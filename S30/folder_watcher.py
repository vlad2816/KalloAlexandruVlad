from pathlib import Path
import shutil
import time


WATCHED_DIR = Path(
    "C:\\Users\\Vlad\\Desktop\\programare curs\\vs code\\S30\\downloads")
TARGET_DIR = Path(
    "C:\\Users\\Vlad\\Desktop\\programare curs\\vs code\\S30\\clean_downloads")

CATEGORY_MAP = {
    "audio": ["mp3", "wav", "flac"],
    "doc": ["doc", "docx", "xls", "pdf"],
    "photo": ["jpg", "jpeg" "png", "bmp"]
}


def categorize(file_path: Path, category: str):
    category_dir = TARGET_DIR / category
    category_dir.mkdir(exist_ok=True)

    file_name = file_path.name
    dst_path = category_dir / file_name

    shutil.copy2(str(file_path), str(dst_path))  # REVEZI Shutil


def get_category(path: Path):
    extension = path.suffix.strip(".")
    for k, v in CATEGORY_MAP.items():
        if extension.lower() in v:
            return k
    return "Its other category"


def walk(root_dir: Path):
    for path in root_dir.iterdir():
        if path.is_file():
            # Sa ma uit iar de ce nu merge.
            categorize(path, get_category(path))


def watch(dir: Path):

    prev_m_time = dir.stat().st_mtime

    while True:
        time.sleep(0.1)
        m_time = dir.stat().st_mtime

        if m_time > prev_m_time:
            print("Dir modificat")
            prev_m_time = m_time


walk(WATCHED_DIR)
