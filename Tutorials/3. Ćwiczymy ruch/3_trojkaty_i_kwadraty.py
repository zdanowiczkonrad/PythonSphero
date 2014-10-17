# -*- coding: utf-8 -*-
from sphero import core
import time
s = core.Sphero("/dev/tty.Sphero-OOB-AMP-SPP")
s.connect()
print "połączyłem się ze Sphero :)"

"""
O ruchu wiadomo już wszystko :)
1 Znajdź błąd w tym programie, który powoduje, że Sphero nie zakreśla kształtu trójkąta
2 Popraw program, aby Sphero jechało w kształcie trójkąta!
3 Zmodyfikuj listę kroków, aby Sphero przejechało drogę w kształcie kwadratu
"""

predkosc = 60
czas = 1

for obrot in [1,120,1]:
	s.roll(predkosc,obrot)
	time.sleep(czas)

# pamiętaj o stop na końcu!
print "stop!"
s.stop()

print "koniec."