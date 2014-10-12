from sphero import core 	# this line imports Sphero controller
import time					# this lines imports time utils

s = core.Sphero("/dev/tty.Sphero-OOB-AMP-SPP") #create Sphero controller
print "Connecting to Sphero..."
s.connect()	#initialize connection

speed = 0x88 # speed of movement
sleep_time=0.1 # how long will each segment last
def make_a_step(current_angle):
	s.roll(speed,current_angle)
	time.sleep(sleep_time)

def make_a_circle(steps):
	rotate_by=int(360/steps)
	current_angle=1
	i=0
	while i<steps:
		make_a_step(current_angle%360)
		current_angle+=rotate_by
		i+=1



i=1
steps=10
while i>0:
	make_a_circle(steps)
	time.sleep(0.1) #sleep 1 seconds
	i-=1

print "The end. Sphero goes to bed."
#s.sleep()



