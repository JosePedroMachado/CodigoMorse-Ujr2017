from sense_hat import SenseHat, ACTION_PRESSED, ACTION_RELEASED

from subprocess import Popen
from time import sleep, process_time

import smtplib
from getpass import getpass
from smtplib import SMTP_SSL
from email.header import Header
from email import encoders
from email.mime.text import MIMEText

sense = SenseHat()
espaco = " "
ponto = "."
linha = "-"
login, password = "hackatonmorse@gmail.com", "...---..."
recipients = [login]
histfile = "/home/pi/historico.txt"

r = [255,0,0]
y = [0,255,255]
g = [0,255,0]
k = [0,0,0]
w = [255,255,255]


dot = [
	k,k,k,k,k,k,k,k,
        k,k,k,k,k,k,k,k,
        k,k,k,k,k,k,k,k,
        k,k,k,w,w,k,k,k,
        k,k,k,w,w,k,k,k,
        k,k,k,k,k,k,k,k,
        k,k,k,k,k,k,k,k,
        k,k,k,k,k,k,k,k,]

line = [
	k,k,k,k,k,k,k,k,
        k,k,k,k,k,k,k,k,
        k,k,k,k,k,k,k,k,
        k,w,w,w,w,w,w,k,
        k,w,w,w,w,w,w,k,
        k,k,k,k,k,k,k,k,
        k,k,k,k,k,k,k,k,
        k,k,k,k,k,k,k,k,]

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

	, "--...--" : "*1"
	, "-.....-" : "*2"
	, "-.---.-" : "*3" }

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
				if event.direction is "left" or event.direction is "up" or event.direction is "down" or event.direction is "right":
					tempo_comeca = process_time()

				if event.direction is "middle":
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

			if event.action is ACTION_RELEASED and tempo_comeca is not 0:
				if process_time() < tempo_comeca + 1: 
					if event.direction is "up":
						print(fr)
						sense.show_message(fr, scroll_speed = 0.04)
						with open(histfile, "a") as f:
							f.write(fr + "\n")
							f.close()

					if event.direction is "left":
						lm += ponto
						print(lm)
						sense.set_pixels(dot)
						sleep(0.5)
						sense.clear()

					if event.direction is "right":
						lm += linha
						print(lm)
						sense.set_pixels(line)
						sleep(0.5)
						sense.clear()

					if event.direction is "down":
						fr += espaco
				else:
					if event.direction is "left":
						Popen(["espeak", "-s", "100", fr])

					if event.direction is "up":
						fr = ""
						lm = ""
						sense.show_message("Apagado", scroll_speed = 0.04)

					if event.direction is "down":
						sai = True
						break

					if event.direction is "right":
						message = fr
						msg = MIMEText(message, 'plain', 'utf-8')
						msg['Subject'] = Header('Mensagem do RPi', 'utf-8')
						msg['From'] = 'RPi <hackatonmorse@gmail.com>'
						msg['To'] = 'hackatonmorse@gmail.com'

						s = SMTP_SSL('smtp.gmail.com', 465)
						s.set_debuglevel(1)
						s.login(login, password)
						s.sendmail(msg['From'], recipients, msg.as_string())
						s.quit()

				tempo_comeca = 0

