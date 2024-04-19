import re
import time
import pendulum
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from loguru import logger
import random
from sqlalchemy import MetaData, Table, select, func

"""
## Clien 크롤러 ##
- 사용 유의사항
카테고리와 검색할 키워드를 묶어서 매개변수로 전달해줘야함
ex. targets = [
                (keyword, category)
                for category in self._cat_list
                for keyword in keywords
            ]
            for target in targets:
                keyword, category = target

- 사용 순서
check_borad_sn > start_beautifulsoup > crawling_posts > check_next_page > crawling_post_detail_list
> 디비 적재 > 페이지가 더 있다면 처음부터 다시 시작(페이지 추가)

"""
tz = pendulum.timezone("Asia/Seoul")


class ClienCrawler:
    def __init__(self, date_from, date_until):
        DEFAULT_DT = pendulum.yesterday(tz=tz)

        self._user_agent = UserAgent(min_percentage=1.1, os=["windows", "macos"])
        self._session = requests.session()
        self._max_board_sn = 0
        self._min_board_sn = 0
        self._base_url = "https://www.clien.net"

        self._date_from = pendulum.parse(date_from) if date_from else DEFAULT_DT
        _date_until = pendulum.parse(date_until) if date_until else DEFAULT_DT
        self._date_until = _date_until.strftime("%Y-%m-%d 23:59:59")

    def check_board_sn(self, keyword, category, table, engine):
        """
        keyword 및 category에 해당하는 board_sn컬럼의 max, min 값을 가져오는 컬럼
        """

        metadata = MetaData()
        metadata.bind = engine
        table = Table(table, metadata, autoload_with=engine)

        stmt = select(func.max(table.c.board_sn), func.min(table.c.board_sn)).where(
            (table.c.category_name == category) & (table.c.keyword == keyword)
        )

        with engine.begin() as connection:
            result = connection.execute(stmt)
            a = result.fetchall()
            max_board_sn = a[0][0] or 0
            min_board_sn = a[0][1] or 0

        return max_board_sn, min_board_sn

    def start_beautifulsoup(self, keyword: str, category: str, page: int):
        headers = {"User-agent": self._user_agent.random}
        target_url = self._base_url + "/service/search"
        keyword_r = keyword.replace("&", "%26").replace("(", "").replace(")", "")
        params = {
            "q": keyword_r,
            "p": page,
            "sort": "recency",
            "boardCd": category,
            "isBoard": True,
        }

        response = self._session.get(
            target_url, headers=headers, params=params, timeout=3
        )
        time.sleep(random.uniform(1, 10))

        soup = BeautifulSoup(response.text, "html.parser")
        return soup

    def crawling_posts(self, soup: BeautifulSoup, keyword: str, category: str):
        """
        게시물들의 기본적인 내용 크롤링
        """
        items = soup.select(".list_item.symph_row.jirum")
        results = []

        for item in items:
            board_sn = int(item["data-board-sn"])
            regist_date = pendulum.parse(item.select_one(".timestamp").text)

            title = item.select_one(".subject_fixed").text
            if "헤드라인 모음" in title:
                continue

            if self._min_board_sn <= board_sn <= self._max_board_sn:
                continue

            if self._date_from < regist_date < pendulum.parse(self._date_until):
                comment = int(item["data-comment-count"])
                url = self._base_url + item.select_one(".subject_fixed")["href"]

                data = {
                    "category_name": category,
                    "regist_date": regist_date,
                    "comment": comment,
                    "url": url,
                    "keyword": keyword,
                    "board_sn": board_sn,
                }
                results.append(data)
        return results

    def check_next_page(self, soup: BeautifulSoup):
        pages = soup.select(".board-nav-page")
        if len(pages) <= 1:
            return None
        next_btn_exists = bool(soup.select_one(".board-nav-next"))

        last_item = soup.select(".list_item")[-1]
        last_item_timestamp = last_item.select_one(".timestamp").text

        if self._date_from > pendulum.parse(last_item_timestamp):
            return None

        for idx, page in enumerate(pages):
            if "active" in page.get("class", []):
                if next_btn_exists or idx + 1 < len(pages):
                    return idx + 1
                break
        return None

    def crawling_post_detail_list(self, posts):
        """
        해당 게시물의 디테일한 내용 가져와서 리스트에 저장
        """
        results = []
        for post in posts:
            logger.info(f"[적재하는 url: {post['url']}")

            details = self._crawling_post_detail(post.get("url"))
            results.append({**post, **details})
        return results

    def _crawling_post_detail(self, post_url):
        """
        해당 게시물의 디테일한 내용 정제하기
        """
        headers = {"User-agent": self._user_agent.random}
        response = self._session.get(post_url, headers=headers)
        time.sleep(random.uniform(1, 10))

        soup = BeautifulSoup(response.text, "html.parser")

        title_elems = soup.select(".post_subject span")
        title = next(
            (
                elem.text.strip()
                for elem in title_elems
                if "post_category" not in elem.get("class", [])
            ),
            None,
        )

        view = soup.select_one(".view_count strong").text.strip().replace(",", "")

        contents = soup.select_one(".post_article").text.strip()
        # 연속된 두 개 이상의 개행을 한 개의 개행으로 줄임
        contents = re.sub(r"\n\n", "\n", contents)
        # 개행 문자를 공백으로 치환
        contents = re.sub(r"\n", " ", contents)
        # \xa0, \xad, \ufeff 문자 제거
        contents = re.sub(r"[\xa0\xad\ufeff]+", "", contents)
        # 두 개 이상의 공백을 단일 공백으로 치환
        contents = re.sub(r" {2,}", " ", contents)

        return {"view": int(view), "title": title, "contents": contents}
