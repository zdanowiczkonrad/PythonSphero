# -*- coding: utf-8 -*-
from sphero import core
import time
s = core.Sphero("/dev/tty.Sphero-OOB-AMP-SPP")
s.connect()
print "połączyłem się ze Sphero :)"

"""
1 Zmodyfikuj poprzedni program, aby Sphero przejechało koło.
możesz użyć funkcji range(1,359)
2 utwórz funkcję "jazda(sphero,lista_obrotow)", ktora przyjmie
jako argumenty kulkę i listę obrotów i wykona ruch!
"""

predkosc = 50
czas = 0.3
lista_ruchow=[1,180] # gladkie wprowadzenie w wyciagniecie zmiennej

for obrot in lista_ruchow:
	s.roll(predkosc,obrot)
	time.sleep(czas)

# pamiętaj o stop na końcu!
print "stop!"
s.stop()

print "koniec."