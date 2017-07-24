from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD
import string

sense = SenseHat()

# Lowercase characters are control
table = [
	"ABCDEFGHIJKLMNOPQRSTUVWXYZ",
	"HIJKLMNOPQRSTUVWXYZABCDEFG",
	"NOPQRSTUVWXYZABCDEFGHIJKLM",
	"UVWXYZABCDEFGHIJKLMNOPQRST",
	"0123456789",
	" .,?'!/():;=+-_\"$@",
	# Sim, Não, Corrigir, Mensagem
	"sncm" ] # Localised to Portuguese, change to "yncm" for english
controlchars = list(string.ascii_lowercase)

# Localised to Portuguese, change to "y", "n", "c" and "m" for english
def controlfunc(char, string):
	# This is why I like switch/case statements
	if char is "s":
		return True, string
	if char is "n":
		return True, ""
	if char is "c":
		return False, string[:-1]
	if char is "m":
		sense.show_message(string, scroll_speed = 0.04)
		return False, string
	return False, string

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
		quit, string = controlfunc(table[row][col], string)
	else:
		quit = False
		string += table[row][col]
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
