# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
from sphero_config import sphero

"""
Cześć! To Twój pierwszy program Sphero. Uruchom go,
wywołując w konsoli następującą komendę:

> python 1_hello_sphero.py

I zaobseruj co się dzieje z Kuleczką.
"""

# nadaj Sphero kolor
sphero.set_rgb(255, 0, 0)
print "czerwono!"
sphero.czekaj(5)

sphero.set_rgb(0, 255, 0)
print "zielono!"
sphero.czekaj(5)

sphero.set_rgb(0, 0, 255)
print "niebiesko!"
sphero.czekaj(5)

print "koniec."