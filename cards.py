"""
Uzdevums par kāršu kavu.
"""

import random

MASTI = ["♤", "♡", "♢", "♧"]
RANGI = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]

# 52 vai 32
SKAITS = 52


"""
Izveido algoritmu, kas no dotajiem rangiem un mastiem sarakstā kava saformē visas kārtis.
Ja skaits ir 52, tad rangi sākas ar 2, bet
ja skaits ir 36, tad rangi sākas ar 7.
Piemēru var apskatīt dotajā attēlā cards.png.
"""
def veidoKavu():
    # Saraksts, kurā glabāsies visas kārtis
    kava = []
    # ... tavs algoritms ...
    jaucKartis(kava)


"""
Sajauc kārtis un sadala tās 4 spēlētājiem katram pa 6 kārtīm.
Vienu kārti nedrīkst izdalīt vairākkārt!
Jāizmanto random.choice(list).
"""
def jaucKartis(kava):
    speletajs1 = []
    speletajs2 = []
    speletajs3 = []
    speletajs4 = []
    # ... jaukšanas un sadalīšanas algoritms ...
    print(f"{speletajs1}\n{speletajs2}\n{speletajs3}\n{speletajs4}")
    

veidoKavu()
