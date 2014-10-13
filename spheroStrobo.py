import thread
import time
from sphero import core
import random

sphero = core.Sphero("/dev/tty.Sphero-OOB-AMP-SPP") #create Sphero controller
print "Connecting to Sphero..."
sphero.connect()	#initialize connection

blink_rate=0.001
for i in range(0,10):
	sphero.set_rgb(255,255,255)
	time.sleep(blink_rate)
	sphero.set_rgb(0,0,0)
	time.sleep(blink_rate)
