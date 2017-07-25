from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD
from subprocess import Popen
from vk import *
from morsetoalpha import *
from sensores import *

histfile = "/home/pi/historico.txt"
sense = SenseHat()

menuentries = ["T", "M", "S", "H", "S"]
menuentrieslong = ["Teclado", "Morse", "Sensores", "Historico", "Sair"]
quitentry = 4

def next(cursor, event):
	return False, cursor + 1
def prev(cursor, event):
	return False, cursor - 1

def readhist():
	Popen(["leafpad", histfile])

def nop():
	return

selectact = {
	  0 : vk
	, 1 : morsetype
	, 2 : sensors
	, 3 : readhist
	, 4 : nop }

def select(cursor, event):
	if event.action is ACTION_PRESSED:
		sense.clear()
		num = cursor % len(menuentries)
		selectact[num]()
		if num is quitentry:
			return True, cursor
	return False, cursor

menuact = {
	  "left"   : prev
	, "right"  : next
	, "up"     : prev
	, "down"   : next
	, "middle" : select }

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
