# -*- coding: utf-8 -*-
from sphero import core
import time
s = core.Sphero("/dev/tty.Sphero-OOB-AMP-SPP")
s.connect()
print "połączyłem się ze Sphero :)"

"""
Dodaj kolejny ruch tak, aby Sphero poruszło się w kształcie litery L
"""

predkosc = 50
czas = 4

s.roll(predkosc,1)
time.sleep(czas)

print "uwaga, zakręt!"
# tutaj dodaj kolejny ruch pod kątem 90 stopni


# pamiętaj o stop na końcu!
print "stop!"
s.stop()

print "koniec."