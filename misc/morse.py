
from sense_hat import SenseHat
from time import sleep
sense=SenseHat()
ponto="."
linha="-"
morsetabela={
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
def morse():
	lm=""
	fr=""
	flush = True
	while True:
	    event = sense.stick.wait_for_event(flush)
	    if flush:
	        flush = False
	    
	    if event.action == 'pressed' and event.direction == 'middle':
	        lm += ponto
	        print(lm)
	    
	
	    elif  event.action == "pressed" and event.direction == "down":
	        lm += linha
	        print(lm)
	
	    elif  event.action=="pressed" and event.direction=="left":
	        sense.show_letter((morsetabela[lm]))
	        fr+=(morsetabela[lm])
	        
	        print(morsetabela[lm])
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
	        
	
    
