# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
from sphero_config import sphero

"""
1. Zmodyfikuj ten program, aby kulka coraz jaśniej świeciła na zielono
2. A teraz tak, aby kulka świeciła się coraz jaśniej na biało!
3. Spróbujmy teraz przyspieszyć wygaszanie kulki - 
   - zobacz co się stanie, jeżeli w range(0,255,20) zastąpisz 20 inną liczbą,
   np. 5, 10 lub 50
4. Odwróćmy teraz kolejność! Niech kulka stopniowo gaśnie, a nie się zapala!
"""

for czerwony in range(0, 255, 20):
	sphero.set_rgb(czerwony, 0, 0)

print "koniec."