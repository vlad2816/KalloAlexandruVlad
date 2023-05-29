from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).parent

FILE_PATH = ROOT / "code1.txt"

# ultima data cand a fost modificat un fisier exemplu code1 dupa ce am scris ceva in el
c_time = FILE_PATH.stat().st_mtime

c_date_time = datetime.fromtimestamp(c_time)

print(c_date_time)
