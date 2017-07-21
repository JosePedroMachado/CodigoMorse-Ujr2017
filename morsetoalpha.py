

from sense_hat import SenseHat
from time import sleep, process_time
sense=SenseHat()
ponto="."
linha="-"
morse={
    ".-": "A",
    "-...":"B"
    ,"-.-.":"C"
    ,"-..":"D"
    ,".":"E"
    ,"..-.":"F"
    ,"--.":"G"
    ,"....":"H"
    ,"..":"I"
    ,".---":"J"
    ,"-.-":"K"
    ,".-..":"L"
    ,"--":"M"
    ,"-.":"N"
    ,"---":"O"
    ,".--.":"P"
    ,"--.-":"Q"
    ,".-.":"R"
    ,"...":"S"
    ,"-":"T"
    ,"..-":"U"
    ,"...-":"V"
    ,".--":"W"
    ,"-..-":"X"
    ,"-.--":"Y"
    ,"--..":"Z"
    ,".----":"1"
    ,"..---":"2"
    ,"...--":"3"
    ,"....-":"4"
    ,".....":"5"
    ,"-....":"6"
    ,"--...":"7"
    ,"---..":"8"
    ,"----.":"9"
    ,"-----":"0"}

def morsetype():
	lm=""
	fr=""
	tempo_comeca = 0
	sense.stick.get_events()
	while True:
	    for event in sense.stick.get_events():

		    if tempo_comeca is not 0 and event.action is 'released':
		        if process_time() < tempo_comeca + 2:
		            lm += ponto
		            print(lm)
		        else:
		            sense.show_message("Apagado")
		            fr=""
		            lm=""
		        tempo_comeca = 0
		    
		    if event.action == 'pressed' and event.direction == 'middle':
		        tempo_comeca = process_time()
	
		    elif  event.action == "pressed" and event.direction == "down":
		        lm += linha
		        print(lm)
		
		    elif  event.action=="pressed" and event.direction=="left":
		        if lm in morse:
		            sense.show_letter((morse[lm]))
		            fr+=(morse[lm])
		            print(morse[lm])
		            sleep(2)
		            sense.clear()
		            lm=""
		        else:
		            print ("erro")
		            sense.show_letter("X",[255,0,0])
		            sleep(2)
		            sense.clear()
		            lm=""
		
		    elif  event.action=="pressed" and event.direction=="right":
		        fr+="."
		        print(".")
		        sense.show_message(("."))
		        
		    elif event.action=="pressed" and event.direction=="up":
		        print(fr)
		        sense.show_message((fr))
		
		
		
		

