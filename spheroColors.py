from sphero import core 	
import time			

s = core.Sphero("/dev/tty.Sphero-OOB-AMP-SPP")
print "Connecting to Sphero..."
s.connect()
print "My current color is: " , s.get_rgb().body
iterations=3
while iterations>0:
	print "Setting color to red"
	s.set_rgb(255,0,0)
	print "Setting color to green"
	s.set_rgb(0,255,0)
	print "Setting color to blue"
	s.set_rgb(0,0,255)
	time.sleep(0.1)
	iterations-=1

print "The end. Sphero goes to bed."
s.sleep()



