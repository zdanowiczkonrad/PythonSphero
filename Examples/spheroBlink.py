import thread
import time
from sphero import core
import random

blink_rate = 1

sphero = core.Sphero("/dev/tty.Sphero-OOB-AMP-SPP") #create Sphero controller
print "Connecting to Sphero..."
sphero.connect()	#initialize connection

def start_blinking(sphero,delay):
	count = 0
	while count < 5:
		global blink_rate
		blink_rate-=0.05
		blink_rate=abs(blink_rate)
		sphero.set_rgb(random.randint(0,255),random.randint(0,255),random.randint(0,255))
		time.sleep(blink_rate)
		sphero.set_rgb(0,0,0)
		time.sleep(blink_rate)

try:
   thread.start_new_thread(start_blinking, (sphero, 2) )
except:
   print "Error: unable to start thread"

while 1:
   pass