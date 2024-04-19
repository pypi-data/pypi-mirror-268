import argparse
import multiprocessing
import pathlib
from concurrent.futures import ThreadPoolExecutor
from functools import partial
from typing import List, Optional
from urllib.parse import unquote

from tqdm import tqdm

from grabber.graph import get_for_telegraph
from grabber.khd import get_sources_for_4khd
from grabber.settings import APP_ROOT
from grabber.utils import (
    query_mapping,
    headers_mapping,
    get_url,
    download_images,
    upload_to_telegraph,
    upload_folders_to_telegraph,
)


DEFAULT_THREADS_NUMBER = multiprocessing.cpu_count()
first_query = "div.content-inner img"
media_root = APP_ROOT / "media"


def get_sources(
    sources: List[str],
    entity: str,
    final_dest: Optional[str] = "",
    save_to_telegraph: Optional[bool] = False,
) -> str:
    images_data = {}
    titles = []
    tqdm_sources_iterable = tqdm(
        enumerate(sources),
        total=len(sources),
    )
    query, src_attr = query_mapping[entity]
    headers = headers_mapping.get(entity, None)
    folders = []

    for idx, source_url in tqdm_sources_iterable:
        tqdm_sources_iterable.set_description(f"Retrieving URLs from {source_url}")
        _, tags, _ = get_url(
            source_url,
            headers=headers,
            query=query,
        )

        url_name = unquote(source_url).split("/")[-2]
        title = url_name.strip().rstrip()
        titles.append(title)
        folder_name = url_name
        image_index = f"{idx + 1}".zfill(2)

        if final_dest:
            final_dest_folder = pathlib.Path(final_dest)
            if not final_dest_folder.exists():
                final_dest_folder.mkdir(parents=True, exist_ok=True)
            new_folder = (
                pathlib.Path(f"{media_root}")
                / pathlib.Path(final_dest)
                / f"{image_index}-{folder_name}"
            )
        else:
            new_folder = pathlib.Path(f"{media_root}") / f"{image_index}-{folder_name}"

        if not new_folder.exists():
            new_folder.mkdir(parents=True, exist_ok=True)

        folders.append(new_folder)
        unique_img_urls = set()

        for idx, img_tag in enumerate(tags):
            img_src = img_tag.attrs[src_attr]

            if "xasiat" in img_src:
                img_name: str = img_src.split("/")[-2]
                img_name = img_name.strip().rstrip()
                img_extension: str = img_name.split(".")[-1]
            else:
                img_name: str = img_src.split("/")[-1]
                img_name = img_name.strip().rstrip()
                img_extension: str = img_name.split(".")[-1]

            unique_img_urls.add(
                (title, f"{idx + 1}.{img_extension}", img_src),
            )

        images_data[title] = (unique_img_urls, new_folder)

    futures = []
    with ThreadPoolExecutor(max_workers=DEFAULT_THREADS_NUMBER) as executor:
        for title in titles:
            images_set, folder = images_data[title]
            partial_download = partial(
                download_images, new_folder=folder, headers=headers
            )
            future = executor.submit(partial_download, images_set, title=title)
            futures.append(future)

    title = titles[0]
    for future in tqdm(
        futures,
        total=len(futures),
        desc="Finishing download...",
    ):
        future.result()

    if save_to_telegraph:
        for folder in folders:
            upload_to_telegraph(folder, page_title=title)

    return title


def main():
    parser = argparse.ArgumentParser(
        prog="Pygalume",
        description="""A simple python command line utility to download images""",
        usage="""
        Pygalume - Lyrics Finder

          Usage: pygalume.py [-s/-sources <list of links>]
                             [-e/--entity webtsite name from where it will be download]
                             [-f/--folder folder where to save]\n

          Examples:
            python customers -e xiuren -f xiuren_folder -s https://www.xiuren.org/albums/1
              """,
    )
    parser.add_argument(
        "-e",
        "--entity",
        dest="entity",
        type=str,
        help="webtsite name from where it will be download",
    )
    parser.add_argument(
        "-s",
        "--sources",
        dest="sources",
        type=str,
        nargs="+",
        help="list of links",
    )
    parser.add_argument(
        "-f",
        "--folder",
        dest="folder",
        type=str,
        default="",
        help="folder where to save",
    )
    parser.add_argument(
        "-t",
        "--telegraph",
        dest="telegraph",
        action="store_true",
        help="Publish page to telegraph",
    )
    parser.add_argument(
        "-u",
        "--upload",
        dest="upload",
        action="store_true",
        help="Upload and publish folders to telegraph",
    )

    options = parser.parse_args()
    entity = options.entity
    folder = options.folder
    sources = options.sources
    telegraph = options.telegraph
    upload = options.upload

    getter_mapping = {
        "4khd": get_sources_for_4khd,
        "telegraph": get_for_telegraph,
    }

    if upload:
        upload_folders_to_telegraph(folder_name=folder)
    else:
        getter_images = getter_mapping.get(entity, get_sources)
        getter_images(
            sources=sources,
            entity=entity,
            final_dest=folder,
            save_to_telegraph=telegraph,
        )
