import multiprocessing
import pathlib
from concurrent.futures import ThreadPoolExecutor
from functools import partial
from typing import List, Optional

from casefy.casefy import snakecase
from tqdm import tqdm

from grabber.settings import MEDIA_ROOT
from grabber.utils import (
    query_mapping,
    headers_mapping,
    get_url,
    download_images,
    upload_to_telegraph,
)

DEFAULT_THREADS_NUMBER = multiprocessing.cpu_count()


def get_for_telegraph(
    sources: List[str],
    entity: str,
    final_dest: str | pathlib.Path = "",
    save_to_telegraph: Optional[bool] = False,
) -> None:
    images_data = {}
    titles = []
    tqdm_sources_iterable = tqdm(
        enumerate(sources),
        total=len(sources),
    )
    query, src_attr = query_mapping[entity]
    headers = headers_mapping.get(entity, None)
    folders = []

    if final_dest:
        final_dest_folder = MEDIA_ROOT / final_dest
        if not final_dest_folder.exists():
            final_dest_folder.mkdir(parents=True, exist_ok=True)
            final_dest = final_dest_folder

    for idx, source_url in tqdm_sources_iterable:
        tqdm_sources_iterable.set_description(f"Retrieving URLs from {source_url}")
        _, tags, soup = get_url(
            source_url,
            headers=headers,
            query=query,
        )

        title_tag = soup.select("title")[0]  # type: ignore
        title = title_tag.get_text().strip().rstrip()
        titles.append(title)

        folder_name = snakecase(title)
        folder_name = folder_name.replace("_", "-")
        image_index = f"{idx + 1}".zfill(2)
        folder_name = f"{image_index}-{folder_name}"

        if final_dest:
            new_folder = final_dest / pathlib.Path(folder_name)
        else:
            new_folder = MEDIA_ROOT / pathlib.Path(folder_name)
        print(f"New folder: {new_folder}")

        if not new_folder.exists():
            new_folder.mkdir(parents=True, exist_ok=True)
            print(f"Folder {new_folder} created\n")

        folders.append(new_folder)
        unique_img_urls = set()

        for idx, img_tag in enumerate(tags):
            img_src = img_tag.attrs[src_attr]
            img_name: str = img_src.split("/")[-1]
            img_name = img_name.strip().rstrip()
            if "images.hotgirl.asia" not in img_src:
                unique_img_urls.add(
                    (title, f"{idx + 1}-{img_name}", f"https://telegra.ph{img_src}"),
                )
            else:
                unique_img_urls.add(
                    (title, f"{idx + 1}-{img_name}", img_src),
                )

        images_data[title] = (unique_img_urls, new_folder)

    futures = []
    with ThreadPoolExecutor(max_workers=DEFAULT_THREADS_NUMBER) as executor:
        for title in titles:
            images_set, folder = images_data[title]
            partial_download = partial(download_images, new_folder=folder)
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

    albums_message = ''.join([f'- {title}\n' for title in titles])
    message = f"""
    All images have been downloaded and saved to the specified folder.
    Albums saved are the following:
        {albums_message}
    """
    print(message)
