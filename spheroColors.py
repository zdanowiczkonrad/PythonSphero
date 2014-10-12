from sphero import core 	# this line imports Sphero controller
import time					# this lines imports time utils

s = core.Sphero("/dev/tty.Sphero-OOB-AMP-SPP") #create Sphero controller
print "Connecting to Sphero..."
s.connect()	#initialize connection
print "My current color is: ",s.get_rgb().body
i=3
while i>0:
	print "Setting color to red"
	s.set_rgb(255,0,0)
	print "Setting color to green"
	s.set_rgb(0,255,0)
	print "Setting color to blue"
	s.set_rgb(0,0,255)
	time.sleep(0.1) #sleep 1 seconds
	i-=1

print "The end. Sphero goes to bed."
s.sleep()



