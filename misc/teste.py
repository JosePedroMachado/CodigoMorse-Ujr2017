from sense_hat import SenseHat, ACTION_HELD
from time import process_time

sense = SenseHat()

i = 0
while i < 20:
	for event in sense.stick.get_events():
		if event.action is ACTION_HELD:
			i += 1
		else:
			i = 0
sense.show_message("1")








time_start = 0
naopassou = True

while naopassou:
	for event in sense.stick.get_events():
		if event.action is ACTION_HELD:
			if time_start is 0:
				time_start = process_time()
			time_now = process_time()
			if time_now > time_start + 2:
				naopassou = False
				break
		else:
			if time_start is not 0:
				time_start = 0

sense.show_message("2")
