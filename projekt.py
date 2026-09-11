with open("lakossag_2025.csv", "r", encoding="utf-8")as forras:
    for f in forras:
        adatok= f.strip().split()

kerdes = int(input(""))
def fomenu(a, b, c):
    a = "[1] Megye adatai"
    b="[2] Település típusa"
    c="[3] Kilépés"


