# -*- coding: utf-8 -*-
from __future__ import print_function
from kulka import Kulka


"""
Teraz spróbuj ustawić własne trzy kolory Sphero!
"""

# ustaw swóje trzy ulubione kolory!
# set_rgb(RED,GREEN,BLUE,1)
# RED       0-255
# GREEN     0-255
# BLUE      0-255
# spróbuj różnych kombinacji!


ADDR = 'XX:XX:XX:XX:XX:XX'


with Kulka(ADDR) as kulka:
    kulka.set_rgb(0, 0, 0)
    kulka.czekaj(5)

    kulka.set_rgb(0, 0, 0)
    kulka.czekaj(5)

    kulka.set_rgb(0, 0, 0)
    kulka.czekaj(5)

    print("koniec.")
