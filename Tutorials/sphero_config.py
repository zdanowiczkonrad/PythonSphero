# -*- coding: utf-8 -*-
# Ten plik ustanawia polaczenie ze Sphero
# oraz definuje zmienna sphero, ktora moze
# byc uzywana do komunikacji
from sphero import core
import time
nazwa_sphero = "/dev/tty.Sphero-WYW-AMP-SPP"
# dla windowsa : "COM-3"
# dla linuxa : sparowac MAC adres z linkiem w /dev/
# timeout na połączenie
timeout_na_polaczenie = 10
# utwórz Sphero, które będzie używane w kodzie
sphero = core.Sphero(nazwa_sphero)
# nawiąż połączenie
sphero.connect()
# dodaj customową funkcję czekaj w Sphero
sphero.czekaj = time.sleep
print "[i] Sphero skonfigurowane poprawnie. Jeszcze chwilkę..."
time.sleep(timeout_na_polaczenie)
# wyłącz stabilizację
# sphero.set_stabilization(True)
print "[i] Połączono ze Sphero."
