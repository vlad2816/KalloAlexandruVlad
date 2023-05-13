# script with a true/false output if one file is png or not
import sys
from pathlib import Path

PNG_SIGNATURE = B'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A'
ROOT = Path(__file__).parent


# png_file_path = ROOT / 'algebra_booleana.png'  # (calea catre fisierul dorit )
png_file_path = Path(sys.argv[1])  # Cli exec


def is_png(content):
    signature = content[:8]
    return PNG_SIGNATURE == signature


def get_resolution(_content: bytes):
    # 16-24
    wide = _content[16:20]
    hight = _content[20:24]
    return int(wide.hex(), base=16), int(hight.hex(), base=16)


if not png_file_path.is_file():
    print('File not found')  # Verificare daca este fisier
    sys.exit(1)

try:
    with open(png_file_path, 'rb') as fin:  # rb Read bytes.
        content = fin.read()
        # print(type(content)) #type binary.
        # print(content) # All the binary code from that png picture.
        if is_png(content):  # Apelare functie direct.
            print('This is a Png file.')
            resolution = get_resolution(content)
            print(
                f'The picture have the next resolution: {resolution[0]} x {resolution[1]} ')
except OSError as err:
    print(err)
    sys.exit(1)
