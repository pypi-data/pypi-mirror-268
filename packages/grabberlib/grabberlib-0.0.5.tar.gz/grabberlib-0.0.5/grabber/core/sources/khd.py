import multiprocessing
import pathlib
from concurrent.futures import ThreadPoolExecutor, as_completed
from functools import partial
from typing import List, Optional

from tqdm import tqdm

from grabber.core.settings import MEDIA_ROOT
from grabber.core.utils import (
    query_mapping,
    headers_mapping,
    get_tags,
    download_images,
    upload_to_telegraph,
)

DEFAULT_THREADS_NUMBER = multiprocessing.cpu_count()
page_nav_query = "div.page-link-box li a.page-numbers"


def get_images_from_pagination(url: str, headers: Optional[dict] = None) -> List[str]:
    tags, _ = get_tags(url, headers=headers, query=page_nav_query)
    return [a.attrs["href"] for a in tags if tags]


def get_sources_for_4khd(
    sources: List[str],
    entity: str,
    final_dest: str | pathlib.Path = "",
    save_to_telegraph: bool | None = False,
    **kwargs,
) -> None:
    titles = set()
    tqdm_sources_iterable = tqdm(
        enumerate(sources),
        total=len(sources),
        desc="Retrieving URLs...",
    )
    query, src_attr = query_mapping[entity]
    headers = headers_mapping.get(entity, None)
    folders = set()
    titles_and_folders = set()
    title_folder_mapping = {}

    if final_dest:
        final_dest_folder = MEDIA_ROOT / pathlib.Path(final_dest)
        if not final_dest_folder.exists():
            final_dest_folder.mkdir(parents=True, exist_ok=True)
            final_dest = final_dest_folder

    for idx, source_url in tqdm_sources_iterable:
        current_folder = None
        current_title = None
        folder_name = ""
        urls = [
            source_url,
            *get_images_from_pagination(url=source_url, headers=headers),
        ]
        image_tags = []

        for index, url in enumerate(urls):
            tags, soup = get_tags(
                url,
                headers=headers,
                query=query,
            )
            image_tags.extend(tags or [])

            if index == 0:
                folder_name = soup.select("title")[0].get_text()  # type: ignore
                title = folder_name.strip().rstrip()
                titles.add(title)
                titles_and_folders.add((title, folder_name))
                current_title = title

        if final_dest:
            new_folder = MEDIA_ROOT / final_dest / folder_name
        else:
            new_folder = MEDIA_ROOT / folder_name

        if not new_folder.exists():
            new_folder.mkdir(parents=True, exist_ok=True)

        current_folder = new_folder
        folders.add(current_folder)
        unique_img_urls = set()

        for idx, img_tag in enumerate(image_tags):
            img_src = img_tag.attrs[src_attr]
            img_name: str = img_src.split("/")[-1].split("?")[0]
            img_name = img_name.strip().rstrip()
            unique_img_urls.add((f"{idx + 1}-{img_name}", img_src))
        title_folder_mapping[current_title] = (unique_img_urls, new_folder)

    with ThreadPoolExecutor(max_workers=DEFAULT_THREADS_NUMBER) as executor:
        # Dictionary to hold Future objects
        futures_to_title = {}
        future_counter = 0
        for title, (images_set, folder_dest) in title_folder_mapping.items():
            partial_download = partial(
                download_images,
                new_folder=folder_dest,
                headers=headers,
                title=title,
            )
            future = executor.submit(partial_download, images_set)
            futures_to_title[future] = title
            future_counter += 1

        # Handling futures as they complete
        for future in tqdm(
            as_completed(futures_to_title),
            total=future_counter,
            desc=f"Retrieving {future_counter} tasks of downloading images",
        ):
            future.result()  # Get the result from the future object

    if save_to_telegraph:
        for title, (_, folder_dest) in title_folder_mapping.items():
            upload_to_telegraph(folder_dest, page_title=title)
