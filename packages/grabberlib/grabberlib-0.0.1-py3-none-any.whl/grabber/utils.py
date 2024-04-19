import multiprocessing
import pathlib
import shutil
from typing import Any, Dict, List, Optional, Tuple

import requests
from bs4 import BeautifulSoup, Tag
from casefy.casefy import snakecase
from PIL import Image
from telegraph import Telegraph
from telegraph.exceptions import TelegraphException
from tenacity import retry, wait_chain, wait_fixed
from tqdm import tqdm

from grabber.settings import MEDIA_ROOT

DEFAULT_THREADS_NUMBER = multiprocessing.cpu_count()
first_query = "div.content-inner img"


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
def get_url(
    url,
    headers: Optional[Dict[str, Any]] = None,
    query: Optional[str] = None,
    stream: Optional[bool] = None,
    ) -> Tuple[requests.Response, Optional[List[Tag]], BeautifulSoup]:
    """Wait 3s for 5 attempts
    7s for the next 4 attempts
    9s for the next 3 attempts
    then 15 for all attempts thereafter
    """
    if stream is not None:
        if headers is not None:
            if stream is not None:
                r = requests.get(url, headers=headers, stream=True)
            else:
                r = requests.get(url, headers=headers)
        else:
            if stream is not None:
                r = requests.get(url, stream=True)
            else:
                r = requests.get(url)

        if r.status_code >= 300:
            print(f"Not able to retrieve {url}: {r.status_code}\n")

        return r, [], None
    else:
        if headers is not None:
            r = requests.get(url, headers=headers)
        else:
            r = requests.get(url)

    if r.status_code > 200:
        print(f"Not able to retrieve {url}: {r.status_code}\n")

    soup = BeautifulSoup(r.content, features="lxml")

    if query is None:
        return r, [], soup

    tags = soup.select(query)

    return r, tags, soup


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

        if filename.exists():
            continue

        if headers is None:
            resp, _, _ = get_url(
                image_url,
                stream=True,
            )
        else:
            resp, _, _ = get_url(
                image_url,
                headers=headers,
                stream=True,
            )

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
    except (Exception, TelegraphException):
        return
    if uploaded:
        return uploaded[0]["src"]


def create_page(title: str, html_content: str, telegraph_client: Telegraph) -> str:
    page = telegraph_client.create_page(title=title, html_content=html_content)
    return page["url"]


def upload_to_telegraph(folder: pathlib.Path, page_title: Optional[str] = "") -> str:
    telegraph_client = Telegraph(
        access_token="d3f83ad3b88a5028de2a7a5b53eecad7e7defc2c392b87f5fab0f72cca5d"
    )
    files = sorted(list(folder.iterdir()), key=sort_file)

    if "telegraph" in folder.name:
        title = " ".join(folder.name.rsplit("-")[1:-3])
    else:
        if "-" in folder.name or "_" in folder.name:
            title = " ".join(folder.name.rsplit("-")[1:-1]).title()
        else:
            title = folder.name.title()

    if not title:
        title = page_title or folder.name

    uploaded_files = []
    contents = []
    html_template = """<figure contenteditable="false"><img src="{file_path}"><figcaption dir="auto" class="editable_text" data-placeholder="{title}"></figcaption></figure>"""

    content_file = pathlib.Path(f"{snakecase(title)}.html")
    if content_file.exists():
        content = content_file.read_text()
    else:
        iterable_files = tqdm(files, total=len(files), desc=f"Uploading files for {folder.name}")
        for file in iterable_files:
            uploaded = upload_file(file, telegraph_client=telegraph_client)
            uploaded_files.append(uploaded)

        for idx, uploaded_file in enumerate(uploaded_files):
            image_title = f"{title} - {idx + 1}"
            contents.append(
                html_template.format(file_path=uploaded_file, title=image_title)
            )

        content = "\n".join(contents)
        with open(f"{snakecase(title)}.html", "w") as f:
            f.write(content)

    print(f"Creating page for {title}")
    page_url = create_page(
        title=title, html_content=content, telegraph_client=telegraph_client
    )

    with open("assets/telegraph_pages.txt", "a") as f:
        f.write(f"{title}: {page_url}\n")

    print(f"Page URL: {page_url}")
    return page_url


def upload_folders_to_telegraph(folder_name: Optional[str] = "") -> None:
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

    for folder in folders:
        upload_to_telegraph(folder)

    with open("assets/telegraph_pages.txt", "a") as f:
        f.write("\n\n\n")
