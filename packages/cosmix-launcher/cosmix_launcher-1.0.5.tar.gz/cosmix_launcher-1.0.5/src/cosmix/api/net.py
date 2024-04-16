from . import logger
from . import config
import requests
import tqdm
import os
import crm1


__all__ = (
    "BLOCK_SIZE",
    "download",
    "get_data",
    "get_json",
    "download_crm1_mod",
)


BLOCK_SIZE = 1024
# JoJoJux's autorepo includes Cosmic Quilt as a dependency, which is a problem because it cannot be resolved.
# This is a list of mods to ignore dependency resolution of.
IGNORED_DEPS = ["quilt_loader"]


def download(url: str, dest: str) -> bool:
    stream = requests.get(url, stream = True)
    size = int(stream.headers.get("content-length", 0))

    logger.debug("Downloading: " + url)

    with tqdm.tqdm(total = size, unit = "B", unit_scale = True) as bar:
        folder = os.path.dirname(dest)
        if not os.path.exists(folder):
            os.makedirs(folder, exist_ok = True)

        with open(dest, "wb") as file:
            for data in stream.iter_content(BLOCK_SIZE):
                bar.update(len(data))
                file.write(data)

    if size != 0 and bar.n != size:
        logger.error("Failed to download file: " + url)

        prompt = f"Remove failed file ({dest})? (y/n) "
        i = input(prompt).lower()
        while i not in {"y", "n"}:
            i = input(prompt).lower()

        if i == "y":
            os.remove(dest)
            logger.info("Removed " + dest)

        return False

    return True


def get_data(url: str) -> str:
    return requests.get(url).text


def get_json(url: str) -> dict:
    return requests.get(url).json()


def download_crm1_mod(mod: str, dest_folder: str, repos: list[str]):
    pool = crm1.RepositoryPool.make([crm1.Repository.from_address(repo) for repo in repos])

    if config.get_config()["crm1"]["use_autorepo_mapping"]:
        for mapping in crm1.autorepotools.get_all_repos():
            pool.add_repository(mapping)

    mod = pool.get_mod(mod)

    if mod is None:
        logger.error(f"Failed to find mod '{mod.id}' in repo pool")
        return

    download(mod.meta.url, os.path.join(dest_folder, mod.id + ".jar"))

    for dep_data in mod.depends:
        if dep_data.id in IGNORED_DEPS:
            continue

        dep = pool.get_mod(dep_data.id)
        if dep is None:
            logger.error(f"Failed to resolve dependency '{dep_data.id}' of mod '{mod.id}' in repo pool")
            return

        download(dep.meta.url, os.path.join(dest_folder, dep.id + ".jar"))
