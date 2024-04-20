import multiprocessing
import pathlib
import shutil
from concurrent.futures import ThreadPoolExecutor, as_completed
from functools import partial
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple

import requests
from bs4 import BeautifulSoup, Tag
from casefy.casefy import snakecase
from lxml import etree
from PIL import Image
from telegraph import Telegraph
from telegraph import exceptions
from tenacity import retry, wait_chain, wait_fixed
from tqdm import tqdm

from grabber.core.settings import MEDIA_ROOT

DEFAULT_THREADS_NUMBER = multiprocessing.cpu_count()
PAGINATION_QUERY = "div.jeg_navigation.jeg_pagination"
PAGINATION_PAGES_COUNT_QUERY = f"{PAGINATION_QUERY} span.page_info"
PAGINATION_BASE_URL_QUERY = "div.jeg_navigation.jeg_pagination a.page_number"
POSTS_QUERY_XPATH = "/html/body/div[2]/div[5]/div/div[1]/div/div/div[2]/div/div/div[2]/div/div[1]/div/div/div/article/div/div/a"


query_mapping = {
    "xiuren": ("div.content-inner img", "src"),
    "nudebird": ("div.thecontent a", "href"),
    "nudecosplay": ("div.content-inner img", "src"),
    "v2ph": ("div.photos-list.text-center img", "src"),  # Needs to handle pagination
    "cgcosplay": ("div.gallery-icon.portrait img", "src"),
    "mitaku": ("img.msacwl-img", "data-lazy"),
    "xasiat": ("div.images a", "href"),
    "telegraph": ("img", "src"),
    "4khd": (
        "div.is-layout-constrained.entry-content.wp-block-post-content img",
        "src",
    ),
    "yellow": (
        "div.elementor-widget-container a[href^='https://terabox.com']",
        "href",
    ),
}


@dataclass(kw_only=True)
class Pagination:
    pagination_query: str
    pages_count_query: str
    pagination_base_url_query: str
    posts_query_xpath: str

    def __post_init__(self) -> None:
        self.pages_count_query = f"{self.pagination_query} {self.pages_count_query}"


query_pagination_mapping = {
    "xiuren": Pagination(
        pagination_query="div.jeg_navigation.jeg_pagination",
        pages_count_query="span.page_info",
        pagination_base_url_query="div.jeg_navigation.jeg_pagination a.page_number",
        posts_query_xpath=(
            "/html/body/div[2]/div[5]/div/div[1]/div/div/div[2]/"
            "div/div/div[2]/div/div[1]/div/div/div/article/div/div/a"
        ),
    ),
    "yellow": Pagination(
        pagination_query="div.jeg_navigation.jeg_pagination",
        pages_count_query="span.page_info",
        pagination_base_url_query="div.jeg_navigation.jeg_pagination a.page_number",
        posts_query_xpath=(
            "/html/body/div[3]/div[4]/div/div[1]/div/div/div[2]/"
            "div/div/div[2]/div/div[1]/div/div/div/article/div/div/a"
        ),
    ),
}
headers_mapping = {
    "nudebird": {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    },
    "v2ph": {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    },
    "cgcosplay": {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    },
    "mitaku": {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    },
    "xasiat": {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    },
    "4khd": {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    },
}


@retry(
    wait=wait_chain(
        *[wait_fixed(3) for _ in range(5)]
        + [wait_fixed(7) for _ in range(4)]
        + [wait_fixed(9) for _ in range(3)]
        + [wait_fixed(15)],
    ),
    reraise=True,
)
def get_image_stream(
    url,
    headers: Optional[Dict[str, Any]] = None,
) -> requests.Response:
    """Wait 3s for 5 attempts
    7s for the next 4 attempts
    9s for the next 3 attempts
    then 15 for all attempts thereafter
    """
    if headers is not None:
        r = requests.get(url, headers=headers, stream=True)
    else:
        r = requests.get(url, stream=True)

    if r.status_code >= 300:
        raise Exception(f"Not able to retrieve {url}: {r.status_code}\n")

    return r


@retry(
    wait=wait_chain(
        *[wait_fixed(3) for _ in range(5)]
        + [wait_fixed(7) for _ in range(4)]
        + [wait_fixed(9) for _ in range(3)]
        + [wait_fixed(15)],
    ),
    reraise=True,
)
def get_tags(
    url,
    query: str,
    headers: Optional[Dict[str, Any]] = None,
) -> Tuple[List[Tag], BeautifulSoup]:
    """Wait 3s for 5 attempts
    7s for the next 4 attempts
    9s for the next 3 attempts
    then 15 for all attempts thereafter
    """
    soup = get_soup(target_url=url, headers=headers)
    tags = soup.select(query)

    return tags, soup


def get_soup(
    target_url: str,
    headers: dict[str, str] | None = None,
) -> BeautifulSoup:
    response = requests.get(target_url, headers=headers)
    return BeautifulSoup(response.content, features="lxml")


def download_images(
    images_set,
    new_folder: pathlib.Path,
    title: str,
    headers: Optional[Dict[str, str]] = None,
):
    """Download an image from a given URL and save it to the specified filename.

    Parameters
    ----------
    - image_url: The URL of the image to be downloaded.
    - filename: The filename to save the image to.

    """

    tqdm_iterable = tqdm(
        images_set,
        total=len(images_set),
        desc=f"Downloading images for {title}",
    )

    for img_name, image_url in tqdm_iterable:
        filename = new_folder / f"{img_name}"

        temp_filename = None
        if filename.suffix == ".webp":
            temp_filename = pathlib.Path(f"{filename.name}.jpg")
            if temp_filename.exists():
                continue

        resp = get_image_stream(image_url, headers=headers)

        with open(filename.as_posix(), "wb") as img_file:
            resp.raw.decode_content = True
            shutil.copyfileobj(resp.raw, img_file)

    convert_from_webp_to_jpg(new_folder)
    return "Done"


def sort_file(file: pathlib.Path) -> str:
    filename = file.name.split(".")[0]
    filename = filename.zfill(2)
    return filename


def convert_from_webp_to_jpg(folder: pathlib.Path) -> None:
    files = list(folder.iterdir())
    tqdm_iterable = tqdm(
        files,
        total=len(files),
        desc="Converting images from WebP to JPEG",
        leave=False,
    )

    for file in tqdm_iterable:
        if file.suffix == ".webp":
            image = Image.open(file).convert("RGB")
            new_file = file.with_suffix(".jpg")
            image.save(new_file, "JPEG")
            file.unlink()


def upload_file(file: pathlib.Path, telegraph_client: Telegraph) -> Optional[str]:
    try:
        uploaded = telegraph_client.upload_file(file)
    except (Exception, exceptions.TelegraphException):
        return
    if uploaded:
        return uploaded[0]["src"]


def create_page(title: str, html_content: str, telegraph_client: Telegraph) -> str:
    page = telegraph_client.create_page(title=title, html_content=html_content)
    return page["url"]


def upload_to_telegraph(
    folder: pathlib.Path,
    page_title: Optional[str] = "",
) -> str:
    telegraph_client = Telegraph(
        access_token="d3f83ad3b88a5028de2a7a5b53eecad7e7defc2c392b87f5fab0f72cca5d"
    )
    files = sorted(list(folder.iterdir()), key=sort_file)
    title = page_title or folder.name
    title = title.strip().rstrip()

    contents = []
    files_urls = []
    html_template = """<figure contenteditable="false"><img src="{file_path}"><figcaption dir="auto" class="editable_text" data-placeholder="{title}"></figcaption></figure>"""

    uploaded_files_url_path = pathlib.Path(f"{snakecase(title)}.txt")
    if uploaded_files_url_path.exists():
        files_urls = uploaded_files_url_path.read_text().split("\n")
    else:
        iterable_files = tqdm(
            files,
            total=len(files),
            desc=f"Uploading files for {folder.name}",
            leave=False,
        )
        image_title = f"{title}"
        for file in iterable_files:
            file_url = upload_file(file, telegraph_client=telegraph_client)
            if not file_url:
                continue
            files_urls.append(file_url)
            contents.append(html_template.format(file_path=file_url, title=image_title))

    content = "\n".join(contents)
    try:
        page_url = create_page(
            title=title,
            html_content=content,
            telegraph_client=telegraph_client,
        )
    except exceptions.TelegraphException as exc:
        print(f"Error: {exc} - {title} - {folder}")
        if "None" not in content:
            with open(uploaded_files_url_path, "w") as f:
                f.write("\n".join(files_urls))
        return

    with open("assets/pages.txt", "a") as f:
        f.write(f"{title} - {page_url}\n")

    return page_url


def upload_folders_to_telegraph(
    folder_name: Optional[str] = "",
    limit: Optional[int] = 0,
) -> None:
    folders = []

    if folder_name:
        root = MEDIA_ROOT / folder_name
        folders += [f for f in list(root.iterdir()) if f.is_dir()]
    else:
        root_folders = [folder for folder in MEDIA_ROOT.iterdir() if folder.is_dir()]
        for folder in root_folders:
            if folder.is_dir():
                nested_folders = [f for f in folder.iterdir() if f.is_dir()]
                if nested_folders:
                    folders += nested_folders
                else:
                    folders = root_folders

    futures_to_folder = {}
    selected_folders = folders[:limit] if limit else folders
    with ThreadPoolExecutor(max_workers=DEFAULT_THREADS_NUMBER) as executor:
        future_counter = 0
        for folder in selected_folders:
            partial_upload = partial(upload_to_telegraph, folder)
            future = executor.submit(partial_upload)
            futures_to_folder[future] = folder
            future_counter += 1

        page_urls: list[tuple[str, str]] = []
        for future in tqdm(
            as_completed(futures_to_folder),
            total=future_counter,
            desc=f"Uploading {future_counter} albums to Telegraph...",
        ):
            result = future.result()
            page_urls.append(result)

        content = "\n".join([f"{page_url}" for page_url in page_urls])
        print(content)


def get_pages_from_pagination(url: str, target: str) -> List[str]:
    pagination_params = query_pagination_mapping[target]
    source_urls = []
    soup = get_soup(url)
    dom = etree.HTML(str(soup))
    pagination_set = soup.select(pagination_params.pages_count_query)
    if not pagination_set:
        return []

    pagination = pagination_set[0]
    pagination_text = pagination.text
    first, last = pagination_text.split("Page")[-1].strip().split("of")
    first_page, last_page = int(first), int(last)

    first_link_pagination = soup.select(pagination_params.pagination_base_url_query)[0]
    href = first_link_pagination.attrs["href"]
    base_pagination_url = href.rsplit("/", 2)[0]

    for a_tag in dom.xpath(pagination_params.posts_query_xpath):
        source_urls.append(a_tag.attrib["href"])

    for index in range(first_page, last_page + 1):
        if index == 1:
            continue

        target_url = f"{base_pagination_url}/{index}/"

        soup = get_soup(target_url)
        dom = etree.HTML(str(soup))
        source_urls.extend(
            [
                a_tag.attrib["href"]
                for a_tag in dom.xpath(pagination_params.posts_query_xpath)
            ]
        )

    return source_urls
