from sphero import core 	# this line imports Sphero controller
import time					# this lines imports time utils



def doTheDance():
	speed=0x88
	sleepTime=1
	s.roll(speed,1)
	time.sleep(sleepTime)
	s.roll(speed,90)
	time.sleep(sleepTime)
	s.roll(speed,180)
	time.sleep(sleepTime)
	s.roll(speed,270)
	time.sleep(sleepTime)


s = core.Sphero("/dev/tty.Sphero-OOB-AMP-SPP") #create Sphero controller
print "Connecting to Sphero..."
s.connect()	#initialize connection
i=3
while i>0:
	doTheDance()
	time.sleep(0.1) #sleep 1 seconds
	i-=1

print "The end. Sphero goes to bed."
#s.sleep()



