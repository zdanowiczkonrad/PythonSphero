# -*- coding: utf-8 -*-
from sphero import core
import time
s = core.Sphero("/dev/tty.Sphero-OOB-AMP-SPP")
s.connect()
print "połączyłem się ze Sphero :)"

"""
1. Umieść napisany przez Ciebie kod w pętli,
aby Sphero trzykrotnie przejechało w tą i z powrotem!
2. Z każdym kolejnym powtórzeniem, zmień prędkość Sphero!
 Wykorzystaj do tego tablicę "predkosci"
4. Z każdym kolejnym powtórzeniem, zmień kolor Sphero!
 Wykorzystaj do tego słownik "kolory" i funkcję set_rgb()
4. Dodaj własny krok z marchewkowym kolorem i prędkością 128
"""
predkosci = [100,40,80]
kolory = [
{'r': 150, 'g': 210, 'b': 54},
{'r': 251, 'g': 61, 'b': 10},
{'r': 70, 'g': 51, 'b': 211}]

predkosc = 80
czas = 1.8

# umieść ten kod w pętli

s.roll(predkosc,1)
time.sleep(czas)
s.roll(predkosc,180)
time.sleep(czas)

# zatrzymujemy kulka
s.stop()
print "koniec."