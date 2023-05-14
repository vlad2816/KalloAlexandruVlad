from lib.interface import CLIMenu
from lib.complaint import Complaint
from pathlib import Path
import pickle

ROOT = Path(__file__).parent

menu = CLIMenu('Complaint booklet', {
    "Adauga plangere": lambda: print("Adauga Plangere"),
    "Rezolva plangere": lambda: print("Rezolva Plangere"),
    "Vezi plangeri nerezolvate": lambda: print("Vezi plangere")
})

# menu.show_main()


# c1 = Complaint("Am o problema1", "Random text here fsdfsad")
# c2 = Complaint("Am o problema2", "Random text here fsdfsad")
# c3 = Complaint("Am o problema3", "Random text here fsdfsad")
# c4 = Complaint("Am o problema4", "Random text here fsdfsad")
# c5 = Complaint("Am o problema5", "Random text here fsdfsad")

# l1 = [c1, c2, c3, c4, c5]

# for i in l1:
#     print(i.id, i.title)

# try:
#     with open(ROOT / 'Complaints.dump', 'wb') as fout:
#         pickle.dump(l1, fout)
# except OSError as err:
#     print(err)

dump_file = ROOT / 'Complaints.dump'

try:
    with open(dump_file, 'rb') as fin:
        unknown = pickle.load(fin)
except OSError as err:
    print(err)
else:
    for i in unknown:
        print(i.id, i.title)
