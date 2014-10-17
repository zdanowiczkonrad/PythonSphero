# -*- coding: utf-8 -*-
# trochę magii - odcinek 1
from sphero import core
import time

# trochę magii - odcinek 2 - połącz się ze Sphero
s = core.Sphero("/dev/tty.Sphero-OOB-AMP-SPP")
s.connect()
print "połączyłem się ze Sphero :)"

"""
Sphero jest zawstydzone! Uruchom ten program i zobacz
jak kuleczka się czerwieni.
"""

for czerwony in range(255):
		if(czerwony % 10 == 0):
			s.set_rgb(czerwony,0,0)
			time.sleep(0.005)

print "koniec."