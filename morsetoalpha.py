from sense_hat import SenseHat, ACTION_PRESSED, ACTION_RELEASED
from subprocess import call
from time import sleep, process_time

sense = SenseHat()
espaco = " "
ponto = "."
linha = "-"

r = [255,0,0]
y = [0,255,255]
g = [0,255,0]
k = [0,0,0]


happyface = [
	k,k,k,k,k,k,k,k,
	k,k,k,k,k,k,k,k,
	k,g,g,k,k,g,g,k,
	k,k,k,k,k,k,k,k,
	k,k,k,k,k,k,k,k,
	k,g,k,k,k,k,g,k,
	k,k,g,g,g,g,k,k,
	k,k,k,k,k,k,k,k ]

normalface = [
	k,k,k,k,k,k,k,k,
	k,k,k,k,k,k,k,k,
	k,y,y,k,k,y,y,k,
	k,k,k,k,k,k,k,k,
	k,k,k,k,k,k,k,k,
	k,k,k,k,k,k,k,k,
	k,k,y,y,y,y,k,k,
	k,k,k,k,k,k,k,k ]

sadface = [
	k,k,k,k,k,k,k,k,
	k,k,k,k,k,k,k,k,
	k,r,r,k,k,r,r,k,
	k,k,k,k,k,k,k,k,
	k,k,k,k,k,k,k,k,
	k,k,k,k,k,k,k,k,
	k,k,r,r,r,r,k,k,
	k,r,k,k,k,k,r,k ]

morse = {
	  ".-"   : "A"
	, "-..." : "B"
	, "-.-." : "C"
	, "-.."  : "D"
	, "."    : "E"
	, "..-." : "F"
	, "--."  : "G"
	, "...." : "H"
	, ".."   : "I"
	, ".---" : "J"
	, "-.-"  : "K"
	, ".-.." : "L"
	, "--"   : "M"
	, "-."   : "N"
	, "---"  : "O"
	, ".--." : "P"
	, "--.-" : "Q"
	, ".-."  : "R"
	, "..."  : "S"
	, "-"    : "T"
	, "..-"  : "U"
	, "...-" : "V"
	, ".--"  : "W"
	, "-..-" : "X"
	, "-.--" : "Y"
	, "--.." : "Z"

	, ".----" : "1"
	, "..---" : "2"
	, "...--" : "3"
	, "....-" : "4"
	, "....." : "5"
	, "-...." : "6"
	, "--..." : "7"
	, "---.." : "8"
	, "----." : "9"
	, "-----" : "0"

	, ".-.-.-"  : "."
	, "--..--"  : ","
	, "..--.."  : "?"
	, ".----."  : "'"
	, "-.-.--"  : "!"
	, "-..-."   : "/"
	, "-.--."   : "("
	, "-.--.-"  : ")"
	, ".-..."   : "&"
	, "---..."  : ":"
	, "-.-.-."  : ";"
	, "-...-"   : "="
	, ".-.-."   : "+"
	, "-....-"  : "-"
	, "..--.-"  : "_"
	, ".-..-."  : "\""
	, "...-..-" : "$"
	, ".--.-."  : "@"

	, ".-.-"      : "|AA|"
	, ".-.-."     : "|AR|"
	, ".-..."     : "|AS|"
	, "-...-"     : "|BT|"
	, "-.-.-"     : "|CT|"
	, "-.--."     : "|KN|"
	, "...-.-"    : "|SK|"
	, "...-."     : "|SN|"
	, "...---..." : "|SOS|"

	, "--...--" : "*1 happy face"
	, "-.....-" : "*2 normal face"
	, "-.---.-" : "*3 sad face" }

def morsetype():
	lm = ""
	fr = ""
	tempo_comeca = 0
	sai = False

	# Flush events
	sense.stick.get_events()

	while sai is False:
		for event in sense.stick.get_events():
			if event.action is ACTION_PRESSED:
				if event.direction is "up" or event.direction is "middle" or event.direction is "down":
					tempo_comeca = process_time()

				if event.direction is "left":
					if lm in morse:
						if morse[lm][0] is "*":
							if morse[lm][1] is "1":
								sense.set_pixels(happyface)
							if morse[lm][1] is "2":
								sense.set_pixels(normalface)
							if morse[lm][1] is "3":
								sense.set_pixels(sadface)
						else:
							sense.show_message(morse[lm], scroll_speed = 0.04)
							fr += (morse[lm])
							print(morse[lm])
						sleep(2)
						sense.clear()
						lm = ""
					else:
						print("erro")
						sense.show_letter("X", [255,0,0])
						sleep(2)
						sense.clear()
						lm = ""

				if event.direction is "right":
					fr += espaco

			if event.action is ACTION_RELEASED and tempo_comeca is not 0:
				if process_time() < tempo_comeca + 1: 
					if event.direction is "up":
						print(fr)
						sense.show_message(fr, scroll_speed = 0.04)
					if event.direction is "middle":
						lm += ponto
						print(lm)
					if event.direction is "down":
						lm += linha
						print(lm)
				else:
					if event.direction is "up":
						call(["espeak", "-s", "100", fr])
					if event.direction is "middle":
						fr = ""
						lm = ""
						sense.show_message("Apagado", scroll_speed = 0.04)
					if event.direction is "down":
						sai = True
						break
				tempo_comeca = 0
