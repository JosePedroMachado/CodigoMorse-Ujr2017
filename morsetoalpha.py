from sense_hat import SenseHat
from time import sleep, process_time
sense=SenseHat()
ponto="."
linha="-"

r=[255,0,0]
y=[0,255,255]
g=[0,255,0]
b=[0,0,0]
br=[100,100,10]


happyface=[
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,g,g,b,b,g,g,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,g,b,b,b,b,g,b,
    b,b,g,g,g,g,b,b,
    b,b,b,b,b,b,b,b
    ]
normalface=[
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,y,y,b,b,y,y,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,y,y,y,y,b,b,
    b,b,b,b,b,b,b,b
    ]
sadface=[
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,r,r,b,b,r,r,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,r,r,r,r,b,b,
    b,r,b,b,b,b,r,b
        
    ]


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
    ,"-----":"0"
    ,".--..":"SOS"
    ,"-.--.":"_1happyface"
    ,"--..--":"_2normalface"
    ,"..--..":"_3sadface"
    
    }

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
		            if morse[lm][0] is "_":
		                if morse[lm][1] is "1":
		                    sense.set_pixels((happyface))
		                if morse[lm][1] is "2":
		                    sense.set_pixels((normalface))
		                if morse[lm][1] is "3":
		                    sense.set_pixels((sadface))
		            else:
		                sense.show_message((morse[lm]))
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


