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
# zapal tylnia diodke
s.set_back_led_output(255)
predkosc=0

for obrot in [1,120,240,359,1]:
	s.roll(predkosc,obrot)
	print "kulek ustawiony na kąt %s" % obrot
	time.sleep(0.00001)
print "koniec."