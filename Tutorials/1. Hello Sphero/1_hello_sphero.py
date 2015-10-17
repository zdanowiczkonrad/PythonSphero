# -*- coding: utf-8 -*-
from __future__ import print_function
from kulka import Kulka
import time


"""
Cześć! To Twój pierwszy program Sphero. Uruchom go, wywołując w
konsoli następującą komendę:

    $ python 1_hello_sphero.py

I zaobseruj co się dzieje z Kuleczką.
"""


ADDR = 'XX:XX:XX:XX:XX:XX'


with Kulka(ADDR) as kulka:
    # nadaj Sphero kolor
    kulka.set_rgb(255, 0, 0)
    print("czerwono!")
    time.sleep(5)

    kulka.set_rgb(0, 255, 0)
    print("zielono!")
    time.sleep(5)

    kulka.set_rgb(0, 0, 255)
    print("niebiesko!")
    time.sleep(5)

    print("koniec.")
