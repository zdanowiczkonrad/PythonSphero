# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
from sphero_config import sphero

"""
1. Zmodyfikuj poprzedni program, aby Sphero przejechało koło.
	podrasuj listę "lista_obrotow".
	możesz użyć funkcji range(1, 359, 40), która utworzy listę
	liczb od 1 do 359 co 40, czyli [1, 41, 81,...]
2. Utwórz funkcję "jazda(sphero, lista_obrotow)" 
	i przenieś do jej definicji pętle for wraz instrukcjami,
	które powodują że Sphero się rolluje i czeka.
3. Zwiększ/zmniejsz czas i zobacz jak Sphero robi mniejsze lub większe koło!
"""

predkosc = 70
czas = 0.5

lista_obrotow = [1, 20, 40, 60]

for obrot in lista_obrotow:
	print "obrot o kat " + str(obrot)
	sphero.roll(predkosc,obrot)
	sphero.czekaj(czas)

# pamiętaj o stop na końcu!
print "stop!"
sphero.stop()

print "koniec."