from pathlib import Path


CACHE_FOLDER_NAME: str = "__joblibcache__"
CACHE_FOLDER_PATH: Path = Path(__file__).parent.joinpath(CACHE_FOLDER_NAME)

if not CACHE_FOLDER_PATH.exists():
    CACHE_FOLDER_PATH.mkdir()
