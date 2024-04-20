import multiprocessing
import pathlib
from concurrent.futures import ThreadPoolExecutor
from functools import partial
from typing import List

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


def get_for_telegraph(
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
    )
    query, src_attr = query_mapping[entity]
    headers = headers_mapping.get(entity, None)
    folders = set()
    titles_and_folders = set()
    title_folder_mapping = {}

    if final_dest:
        final_dest_folder = MEDIA_ROOT / final_dest
        if not final_dest_folder.exists():
            final_dest_folder.mkdir(parents=True, exist_ok=True)
            final_dest = final_dest_folder

    for idx, source_url in tqdm_sources_iterable:
        folder_name = ""
        tags, soup = get_tags(
            source_url,
            headers=headers,
            query=query,
        )

        title_tag = soup.select("title")[0]  # type: ignore
        folder_name = title_tag.get_text().strip().rstrip()
        title = folder_name
        titles.add(title)
        titles_and_folders.add((title, folder_name))

        if final_dest:
            new_folder = MEDIA_ROOT / final_dest / folder_name
        else:
            new_folder = MEDIA_ROOT / folder_name

        if not new_folder.exists():
            new_folder.mkdir(parents=True, exist_ok=True)

        folders.add(new_folder)
        unique_img_urls = set()

        for idx, img_tag in enumerate(tags or []):
            img_src = img_tag.attrs[src_attr]
            img_name: str = img_src.split("/")[-1]
            img_name = img_name.strip().rstrip()
            if "images.hotgirl.asia" not in img_src:
                unique_img_urls.add(
                    (f"{idx + 1}-{img_name}", f"https://telegra.ph{img_src}")
                )
            else:
                unique_img_urls.add((f"{idx + 1}-{img_name}", img_src))

        title_folder_mapping[title] = (unique_img_urls, new_folder)

    futures = []
    with ThreadPoolExecutor(max_workers=DEFAULT_THREADS_NUMBER) as executor:
        for title, (images_set, folder_dest) in title_folder_mapping.items():
            partial_download = partial(
                download_images,
                new_folder=folder_dest,
                headers=headers,
                title=title,
            )
            future = executor.submit(partial_download, images_set, title=title)
            futures.append(future)

    for future in tqdm(
        futures,
        total=len(futures),
        desc="Finishing download...",
    ):
        future.result()

    if save_to_telegraph:
        for folder in folders:
            print(f"Uploading to telegraph {folder}")
            upload_to_telegraph(folder)

    albums_message = "".join([f"- {title}\n" for title in titles])
    message = f"""
    All images have been downloaded and saved to the specified folder.
    Albums saved are the following:
        {albums_message}
    """
    print(message)
