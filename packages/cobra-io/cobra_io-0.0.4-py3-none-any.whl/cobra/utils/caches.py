from pathlib import Path
import shutil

from cobra.utils.configurations import COBRA_CONFIG


MAIN_CACHE_DIR = Path(COBRA_CONFIG['FILE_LOCATIONS']['cache'])
ASSET_CACHE = MAIN_CACHE_DIR.joinpath('assets')
MODULE_DB_CACHE = MAIN_CACHE_DIR.joinpath('module_dbs')
TASK_CACHE = MAIN_CACHE_DIR.joinpath('tasks')
SOLUTION_CACHE = MAIN_CACHE_DIR.joinpath('solutions')
SCHEMA_CACHE = MAIN_CACHE_DIR.joinpath('schemas')
caches = {MAIN_CACHE_DIR, ASSET_CACHE, MODULE_DB_CACHE, TASK_CACHE, SOLUTION_CACHE, SCHEMA_CACHE}


def generate_caches():
    """Creates the cache directories."""
    for dir in caches:
        dir.mkdir(parents=True, exist_ok=True)


def reset_cache():
    """Deletes the cache directory."""
    shutil.rmtree(MAIN_CACHE_DIR)
    generate_caches()


generate_caches()


if __name__ == '__main__':
    val = input("This will delete the cache directory. Press y and enter to continue.")
    if val == 'y':
        reset_cache()
    else:
        print("Aborted.")
