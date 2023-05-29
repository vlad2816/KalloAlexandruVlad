import os
import shutil
from pathlib import Path


ROOT = Path(__file__).parent
PHOTO_PATH = ROOT / "poze_nunta"

# os.rename(ROOT / "code.txt", ROOT / "code1.txt")  # rename file with os module

# print(os.listdir(ROOT)) Iti arata ce ai in directorul respectiv

# for i in ROOT.iterdir():
#     print(i, i.is_dir())   # Asa vad daca in director am folder sau nu.

# for dirpath, dirs, files in os.walk(ROOT):
#     # print(
#     #     f"In directorul {dirpath} am gasit {len(dirs)} directoare si {len(files)} fisiere.")
#     for _file in files:
#         print(Path(dirpath) / _file) Asa vad ce contine si fisierul poze_nunta

count = 0
for i in PHOTO_PATH.glob("*.jpg"):
    # LA fel pot si cu ROOT.glob sa vad tot ce am in fisierul S30 + In adancul fisierului poze_nunta.
    i.rename(PHOTO_PATH / f"Vlad&XADSA-{count}.jpg")
    count += 1
