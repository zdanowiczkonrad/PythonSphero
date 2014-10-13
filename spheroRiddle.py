from random import randint
from sphero import core
import time	
import thread

# this program is a simple implementation of a game,
# where the user is supposed to guess the number
# in a range 1 to 100, while the program can give
# him a hint, whether the number provided is greater,
# equal or less to the one provided by the player

# pulse rate means how close is user to guess the number
# the smaller the value is, the closer the user is.
# range: 0-100

s = core.Sphero("/dev/tty.Sphero-OOB-AMP-SPP") #create Sphero controller
print "Connecting to Sphero..."
s.connect()	#initialize connection

def show_hint_in_sphero(pulse_rate):
	print "pulse rate: %s" % pulse_rate
	green_channel=abs(255-int(pulse_rate*2.55))%255
	color="10,%s,10" % (green_channel)
	s.set_rgb(0,green_channel,0)
	print "color: "+color

def show_hint(difference):
	if difference > 0:
		print "My number is greater!"
	else:
		print "My number is smaller!"
	pulse_rate = abs(difference)
	show_hint_in_sphero(pulse_rate)

def game():
	print """
Welcome to the SpheroRiddle game! Guess my number!
If you want to have a hint about how close you are,
take a look at the Sphero. The faster it blinks and
the brighter it shines, the closer you are.
--------------------------------------------------
Type in the number!
"""

	secret_number=randint(1,100)
	guess=-1
	trials=0
	end=False
	while(not end):
		guess=raw_input("> ")
		if guess == 'q' or guess == 'quit':
			end = True
		elif guess.isdigit():
			guess=int(guess)
			trials = trials + 1
			if secret_number is not guess:
				show_hint(secret_number-guess)
			else:
				print "Bravo! You've guessed my number in %s trials!" % trials
				end=True
		else:
			print "Please input the number or 'q'/'quit' if you want to end the game."

def play_next():
	next=raw_input("Do you want to play another game? (y/n): ").lower()
	return next=="y" or next =="yes"

game()
while play_next():
	game()

