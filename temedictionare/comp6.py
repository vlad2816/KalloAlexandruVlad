# 6. Se da lista de mai jos:
rezultate_campionat = [
    {"echipa": "CFR Cluj", "meciuri_jucate": 36,
        "victorii": 22, "egaluri": 9, "infrangeri": 5},
    {"echipa": "FCSB", "meciuri_jucate": 36,
        "victorii": 21, "egaluri": 7, "infrangeri": 8},
    {"echipa": "Universitatea Craiova", "meciuri_jucate": 36,
        "victorii": 18, "egaluri": 11, "infrangeri": 7},
    {"echipa": "Sepsi Sfântu Gheorghe", "meciuri_jucate": 36,
        "victorii": 15, "egaluri": 11, "infrangeri": 10},
    {"echipa": "Astra Giurgiu", "meciuri_jucate": 36,
        "victorii": 14, "egaluri": 11, "infrangeri": 11},
    {"echipa": "CS Mioveni", "meciuri_jucate": 36,
        "victorii": 13, "egaluri": 12, "infrangeri": 11},
    {"echipa": "FC Argeș Pitești", "meciuri_jucate": 36,
        "victorii": 13, "egaluri": 9, "infrangeri": 14},
    {"echipa": "FC Botoșani", "meciuri_jucate": 36,
        "victorii": 12, "egaluri": 10, "infrangeri": 14},
    {"echipa": "Gaz Metan Mediaș", "meciuri_jucate": 36,
        "victorii": 11, "egaluri": 12, "infrangeri": 13},
    {"echipa": "FC Voluntari", "meciuri_jucate": 36,
        "victorii": 12, "egaluri": 8, "infrangeri": 16},
    {"echipa": "Academica Clinceni", "meciuri_jucate": 36,
        "victorii": 10, "egaluri": 12, "infrangeri": 14},
    {"echipa": "FC Hermannstadt", "meciuri_jucate": 36,
        "victorii": 10, "egaluri": 11, "infrangeri": 15}
]

# avand in vedere ca o victorie valoreaza 3 pct. si un egal 1 pct.

# a) sa se adauge o cheie noua in fiecare dictionar, numele cheii este 'puncte'
# iar ca valoare va avea numarul de puncte acumulate
# b) sa se afiseze numele echipei campioane
# c) sa se afiseze numele echipei cu ele mai multe egaluri
# d) sa se afiseze podiumul (nume si numar de pct)

for i in rezultate_campionat:
    i["puncte"] = i["victorii"] * 3 + i["egaluri"]

campioana = sorted(rezultate_campionat,
                   key=lambda x: x["puncte"], reverse=True)

# ca sa vad doar echipa campioana
print(f'Echipa campioana este: {rezultate_campionat[0]["echipa"]}')

rezultate_campionat.sort(key=lambda x: x["egaluri"], reverse=True)

print(
    f'Echipa cu cele mai multe egaluri este: {rezultate_campionat[0]["echipa"]}')

rezultate_campionat.sort(key=lambda x: x["puncte"], reverse=True)
podium = rezultate_campionat[:3]

for i in podium:
    print(i["echipa"], i["puncte"])
