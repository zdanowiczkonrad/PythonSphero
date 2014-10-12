from sphero import core
import time

s = core.Sphero("/dev/tty.Sphero-OOB-AMP-SPP")
print "Connecting to Sphero..."
s.connect()

def doTheDance():
	speed = 0x88
	sleepTime = 1
	s.roll(speed,1)
	time.sleep(sleepTime)
	s.roll(speed,90)
	time.sleep(sleepTime)
	s.roll(speed,180)
	time.sleep(sleepTime)
	s.roll(speed,270)
	time.sleep(sleepTime)

squares = 3
while squares > 0:
	doTheDance()
	time.sleep(0.1)
	squares -= 1
