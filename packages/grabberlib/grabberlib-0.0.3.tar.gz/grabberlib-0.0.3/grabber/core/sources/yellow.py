import multiprocessing
from typing import List

from lxml import etree

from grabber.core.utils import (
    get_soup,
)

DEFAULT_THREADS_NUMBER = multiprocessing.cpu_count()
PAGINATION_QUERY = "div.jeg_navigation.jeg_pagination"
PAGINATION_PAGES_COUNT_QUERY = f"{PAGINATION_QUERY} span.page_info"
BASE_URL = "https://yellowfever18.com"
TAG_BASE_URL = f"{BASE_URL}/tag"
CSP_TAG_BASE_URL = f"{TAG_BASE_URL}/cosplay"
TAG_PAGINATION_BASE_URL = f"{TAG_BASE_URL}/page"
CSP_TAG_PAGINATION_BASE_URL = f"{CSP_TAG_BASE_URL}/page"
PAGINATION_BASE_URL_QUERY = "div.jeg_navigation.jeg_pagination a.page_number"
POSTS_QUERY_XPATH = "/html/body/div[3]/div[4]/div/div[1]/div/div/div[2]/div[1]/div/div[2]/div/div[1]/div/div/div/article/div/div[1]/a[1]"


def get_pages_from_pagination(url: str) -> List[str]:
    source_urls = []
    soup = get_soup(url)
    dom = etree.HTML(str(soup))
    pagination = soup.select(PAGINATION_PAGES_COUNT_QUERY)[0]
    pagination_text = pagination.text
    first, last = pagination_text.split("Page")[-1].strip().split("of")
    first_page, last_page = int(first), int(last)

    first_link_pagination = soup.select(PAGINATION_BASE_URL_QUERY)[0]
    href = first_link_pagination.attrs["href"]
    base_pagination_url = href.rsplit("/", 2)[0]

    for a_tag in dom.xpath(POSTS_QUERY_XPATH):
        source_urls.append(a_tag.attrib["href"])

    for index in range(first_page, last_page + 1):
        if index == 1:
            continue

        target_url = f"{base_pagination_url}/{index}/"

        soup = get_soup(target_url)
        dom = etree.HTML(str(soup))
        source_urls.extend(
            [a_tag.attrib["href"] for a_tag in dom.xpath(POSTS_QUERY_XPATH)]
        )

    return source_urls
