from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD
from subprocess import Popen
from vk import *
from morsetoalpha import *

historico = '/home/pi/history.txt'
sense = SenseHat()

menuentries = ["T", "M", "S","H"]
menuentrieslong = ["Teclado", "Morse", "Sair","Historico"]

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
			quit = True
		if cursor % len(menuentries) is 3:
			Popen(["leafpad", historico])
			#file = open(historico,'r')
			#sense.show_message(file.read(), scroll_speed = 0.04)
			#print(file.read())
			#file.close()

	return quit, cursor

menuact = {
	"left": prev,
	"right": next,
	"up": prev,
	"down": next,
	"middle": select}

def menu():
	cursor = 0
	quit = False

	sense.show_message(menuentrieslong[0], scroll_speed = 0.04)

	while True:
		sense.show_letter(menuentries[cursor % len(menuentries)])

		# Flush events
		sense.stick.get_events()

		event = sense.stick.wait_for_event()
		if event.action is ACTION_PRESSED or event.action is ACTION_HELD:
			quit, cursor = menuact[event.direction](cursor, event)

		if quit:
			sense.clear()
			return

		if event.action is ACTION_PRESSED:
			sense.show_message(menuentrieslong[cursor % len(menuentrieslong)], scroll_speed = 0.04)

menu()
