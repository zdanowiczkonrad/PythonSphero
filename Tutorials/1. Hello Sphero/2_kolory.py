# -*- coding: utf-8 -*-
# trochę magii - odcinek 1
from sphero import core
import time

# trochę magii - odcinek 2 - połącz się ze Sphero
s = core.Sphero("/dev/tty.Sphero-OOB-AMP-SPP")
s.connect()
print "połączyłem się ze Sphero :)"

"""
Teraz spróbuj ustawić własne trzy kolory Sphero!
"""

# ustaw swóje trzy ulubione kolory!
# set_rgb(RED,GREEN,BLUE,1)
# RED		0-255
# GREEN		0-255
# BLUE		0-255
# spróbuj różnych kombinacji!
s.set_rgb(0,0,0)
time.sleep(5)

s.set_rgb(0,0,0)
time.sleep(5)

s.set_rgb(0,0,0)
time.sleep(5)

print "koniec."