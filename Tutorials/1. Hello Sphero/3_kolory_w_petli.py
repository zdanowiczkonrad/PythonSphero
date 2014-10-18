# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
from sphero_config import sphero

"""
Sphero jest zawstydzone! Uruchom ten program i zobacz
jak kuleczka się czerwieni.
"""

for czerwony in range(0, 255, 20):
	sphero.set_rgb(czerwony, 0, 0)

print "koniec."