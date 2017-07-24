from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

while True:
	event = sense.stick.wait_for_event()
	print("Joystick {} {}".format(event.action, event.direction))
