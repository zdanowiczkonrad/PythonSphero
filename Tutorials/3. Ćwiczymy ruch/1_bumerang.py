# -*- coding: utf-8 -*-
from sphero import core
import time
s = core.Sphero("/dev/tty.Sphero-OOB-AMP-SPP")
s.connect()
print "połączyłem się ze Sphero :)"

"""
Przyszła pora na coś ciekawszego :) Zobacz co dzieje się w tym programie,
i wyjaśnij co robi funkcja roll!
"""
time.sleep(7)
# zapal tylnia diodke
s.set_back_led_output(255)
predkosc = 60
czas = 2

s.roll(predkosc,1)
time.sleep(czas)
s.roll(predkosc,180)
time.sleep(czas)

print "koniec."
