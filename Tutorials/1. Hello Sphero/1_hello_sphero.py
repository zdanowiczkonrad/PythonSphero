# -*- coding: utf-8 -*-
# trochę magii - odcinek 1
from sphero import core
import time
"""
Hej! To Wasze pierwsze spotkanie ze Sphero! Upewnij się,
że Sphero jest sparowane z tą stacją i uruchom ten program,
a następnie przeanalizuj co się tutaj dzieje.
"""
# trochę magii - odcinek 2 - połącz się ze Sphero
s = core.Sphero("/dev/tty.Sphero-OOB-AMP-SPP")
s.connect()
print "połączyłem się ze Sphero :)"

# nadaj Sphero kolor

s.set_rgb(255,0,0)
print "czerwono!"
time.sleep(5)

s.set_rgb(0,255,0)
print "zielono!"
time.sleep(5)

s.set_rgb(0,0,255)
print "niebiesko!"
time.sleep(5)

print "koniec."