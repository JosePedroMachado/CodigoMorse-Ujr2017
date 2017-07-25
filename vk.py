from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD
from subprocess import Popen
from time import sleep
import string

sense = SenseHat()

histfile = "/home/pi/historico.txt"

# Lowercase characters are control
table = [
	"ABCDEFGHIJKLMNOPQRSTUVWXYZ",
	"HIJKLMNOPQRSTUVWXYZABCDEFG",
	"NOPQRSTUVWXYZABCDEFGHIJKLM",
	"UVWXYZABCDEFGHIJKLMNOPQRST",
	"0123456789",
	" .,?'!/():;=+-_\"$@",
	# Sim, Não, Corrigir, Mensagem, Falar
	"sncmf" ] # Localised to Portuguese, change to "yncms" for english
controlchars = list(string.ascii_lowercase)

# Localised to Portuguese, change to "y", "n", "c", "m" and "s" for english
def ctrls(string):
	with open(histfile, "a") as file:
		file.write(string + "\n")
		file.close()
	return True, string
def ctrln(string):
	return True, ""
def ctrlc(string):
	return False, string[:-1]
def ctrlm(string):
	sense.show_message(string, scroll_speed = 0.04)
	return False, string
def ctrlf(string):
	Popen(["espeak", "-s", "100", string])
	return False, string

ctrl = {
	  "s" : ctrls
	, "n" : ctrln
	, "c" : ctrlc
	, "m" : ctrlm
	, "f" : ctrlf }

def curmoveleft(cursor, string):
	cursor[0] -= 1
	return False, string
def curmoveright(cursor, string):
	cursor[0] += 1
	return False, string
def curmoveup(cursor, string):
	cursor[1] -= 1
	return False, string
def curmovedown(cursor, string):
	cursor[1] += 1
	return False, string
def curmovemiddle(cursor, string):
	row = cursor[1] % len(table)
	col = cursor[0] % len(table[row])
	if table[row][col] in controlchars:
		quit, string = ctrl[table[row][col]](string)
	else:
		quit = False
		string += table[row][col]
		sense.show_letter(" ", back_colour = [255, 255, 255])
		sleep(.1)
		sense.clear()
	return quit, string

curmove = {
	  "left"   : curmoveleft
	, "right"  : curmoveright
	, "up"     : curmoveup
	, "down"   : curmovedown
	, "middle" : curmovemiddle }

def vk():
	string = ""
	cursor = [0, 0]

	# Flush events
	sense.stick.get_events()

	sense.show_letter(table[0][0])

	while True:
		event = sense.stick.wait_for_event()
		if event.action is ACTION_PRESSED or event.action is ACTION_HELD:
			quit, string = curmove[event.direction](cursor, string)
			if quit:
				sense.clear() 
				return string
			row = cursor[1] % len(table)
			col = cursor[0] % len(table[row])
			sense.show_letter(table[row][col])
