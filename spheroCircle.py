from sphero import core
import time

s = core.Sphero("/dev/tty.Sphero-OOB-AMP-SPP")
print "Connecting to Sphero..."
s.connect()

speed = 0x88
sleep_time = 0.1 

def make_a_step(current_angle):
	s.roll(speed,current_angle)
	time.sleep(sleep_time)

def make_a_circle(steps):
	rotate_by = int(360/steps)
	current_angle = 1
	i = 0
	while i < steps:
		make_a_step(current_angle%360)
		current_angle += rotate_by
		i += 1

steps=10
make_a_circle(steps)
