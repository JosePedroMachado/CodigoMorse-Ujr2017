from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD
from subprocess import Popen
from vk import *
from morsetoalpha import *
from sensores import *

histfile = "/home/pi/historico.txt"
sense = SenseHat()

menuentries = ["T", "M", "S", "H","S"]
menuentrieslong = ["Teclado", "Morse", "Sensores", "Historico","Sair"]

def next(cursor, event):
	return False, cursor + 1
def prev(cursor, event):
	return False, cursor - 1

def select(cursor, event):
	quit = False
	file = None

	if event.action is ACTION_PRESSED:
		sense.clear()
		if cursor % len(menuentries) is 0:
			print(vk())
		if cursor % len(menuentries) is 1:
			morsetype()
		if cursor % len(menuentries) is 2:
			sensortype()	
		if cursor % len(menuentries) is 3:
			Popen(["leafpad", histfile])
			#file = open(historico,'r')
			#sense.show_message(file.read(), scroll_speed = 0.04)
			#print(file.read())
			#file.close()			
		if cursor % len(menuentries) is 4:
			quit = True

	return quit, cursor

menuact = {
	"left": prev,
	"right": next,
	"up": prev,
	"down": next,
	"middle": select}

def menu():
	cursor = 0
	event = None
	quit = False

	while True:
		# Flush events
		sense.stick.get_events()

		if event is None or event.action is ACTION_PRESSED:
			sense.show_message(menuentrieslong[cursor % len(menuentrieslong)], scroll_speed = 0.04)
			sense.show_letter(menuentries[cursor % len(menuentries)])

		event = sense.stick.wait_for_event()
		if event.action is ACTION_PRESSED or event.action is ACTION_HELD:
			quit, cursor = menuact[event.direction](cursor, event)

		if quit:
			sense.clear()
			return

menu()
