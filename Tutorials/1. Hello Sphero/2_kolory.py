# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
from sphero_config import sphero

"""
Teraz spróbuj ustawić własne trzy kolory Sphero!
"""

# ustaw swóje trzy ulubione kolory!
# set_rgb(RED,GREEN,BLUE,1)
# RED		0-255
# GREEN		0-255
# BLUE		0-255
# spróbuj różnych kombinacji!

sphero.set_rgb(0, 0, 0)
sphero.czekaj(5)

sphero.set_rgb(0, 0, 0)
sphero.czekaj(5)

sphero.set_rgb(0, 0, 0)
sphero.czekaj(5)

print "koniec."