from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD
from time import sleep
from vk import *
from morsetoalpha import *

sense = SenseHat()

# Teclado, Morse, Sair
menuentries = ["T", "M", "S"]

def next(cursor, event):
	return False, False, cursor + 1
def prev(cursor, event):
	return False, False, cursor - 1

def select(cursor, event):
	quit = False
	if event.action is ACTION_PRESSED:
		sense.clear()
		if cursor % len(menuentries) is 0:
			print(vk())
		elif cursor % len(menuentries) is 1:
			morsetype()
		else:
			quit = True
	return True, quit, cursor

menuact = {
	"left": prev,
	"right": next,
	"up": prev,
	"down": next,
	"middle": select
}

def menu():
	cursor = 0
	flush = False
	quit = False
	sense.show_letter(menuentries[0])
	while True:
		event = sense.stick.wait_for_event(flush)
		if flush:
			flush = False
		if event.action is ACTION_PRESSED or event.action is ACTION_HELD:
			flush, quit, cursor = menuact[event.direction](cursor, event)
		if quit:
			sense.clear()
			return
		sense.show_letter(menuentries[cursor % len(menuentries)])

menu()
