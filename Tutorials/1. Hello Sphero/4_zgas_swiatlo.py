# -*- coding: utf-8 -*-
from kulka import Kulka


"""
1. Zmodyfikuj ten program, aby kulka coraz jaśniej świeciła na zielono
2. A teraz tak, aby kulka świeciła się coraz jaśniej na biało!
3. Spróbujmy teraz przyspieszyć wygaszanie kulki -
   - zobacz co się stanie, jeżeli w range(0,255,20) zastąpisz 20 inną liczbą,
     np. 5, 10 lub 50
4. Odwróćmy teraz kolejność! Niech kulka stopniowo gaśnie, a nie się zapala!
"""


ADDR = 'XX:XX:XX:XX:XX:XX'


with Kulka(ADDR) as kulka:
    for czerwony in range(0, 255, 20):
        kulka.set_rgb(czerwony, 0, 0)

print "koniec."
