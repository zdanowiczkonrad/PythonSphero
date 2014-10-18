# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
from sphero_config import sphero

"""
1. Przeanalizuj ten program i narysuj na kartce tor,
	po którym Twoim zdaniem przejedzie Sphero.
2. Następnie uruchom go i porównaj wyniki z przypuszczeniami
"""

predkosc = 60
czas = 2

# bumerang
sphero.roll(predkosc, 1)
sphero.czekaj(czas)

sphero.roll(predkosc, 180)
sphero.czekaj(czas)

print "stop!"
sphero.stop()

print "koniec."
