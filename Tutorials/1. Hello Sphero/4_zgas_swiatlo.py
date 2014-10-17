# -*- coding: utf-8 -*-
# trochę magii - odcinek 1
from sphero import core
import time

# trochę magii - odcinek 2 - połącz się ze Sphero
s = core.Sphero("/dev/tty.Sphero-OOB-AMP-SPP")
s.connect()
print "połączyłem się ze Sphero :)"

"""
1. Zmodyfikuj ten program, aby kulka coraz jaśniej świeciła na zielono
2. A teraz tak, aby kulka świeciła się coraz jaśniej na biało!
3. Spróbujmy teraz przyspieszyć wygaszanie kulki - zobacz
 jak zmiana "% 10 == 0" na większą, np. % 20 lub % 40 wpływa na prędkość gaszenia
4. Odwróćmy teraz kolejność! Niech kulka stopniowo gaśnie a nie się zapala!
"""

for czerwony in range(255):
		if(czerwony % 10 == 0):
			s.set_rgb(czerwony,0,0)
			time.sleep(0.005)

print "koniec."