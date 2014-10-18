# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
from sphero_config import sphero

"""
1. Umieść napisany przez Ciebie kod w pętli,
aby Sphero trzykrotnie przejechało w tę i z powrotem!
2. Z każdym kolejnym powtórzeniem, zmień prędkość Sphero!
 Wykorzystaj do tego listę "predkosci"
3. Z każdym kolejnym powtórzeniem, zmień kolor Sphero!
 Wykorzystaj do listę kolory. funkcję set_rgb()
4. Dodaj własny krok z marchewkowym kolorem i prędkością 128
	- rozszerz listę predkosci o 128, oraz dodaj do tablicy kolory
	kolejny element z własnym kolorem
"""
predkosci = [100, 40, 80]

kolory = [
[150, 210, 54],
[251, 61, 10],
[70, 51, 211]
]

czas = 2

# umieść ten kod w pętli
# ----------------------------------------------------
# 1. ustaw pierwszy kolor z tablicy kolory
sphero.set_rgb(kolory[0][0], kolory[0][1], kolory[0][2])

# 2. zatocz się z prędkością 100
sphero.roll(predkosci[0], 1)
sphero.czekaj(czas)
# 3. wielki powrót
sphero.roll(predkosci[0], 180)
sphero.czekaj(czas)
# ----------------------------------------------------
print "stop!"
sphero.stop()
print "koniec."