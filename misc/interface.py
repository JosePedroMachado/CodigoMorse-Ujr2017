from guizero import App,Text,TextBox,PushButton,Slider,Picture,info

def say_my_name():
    welcome_message.set(my_name.get("Codigo Morse"))
    
app = App("Melhor Projeto 2017")

welcome_message = Text(app, text="Codigo Morse", size=40, color="black")

def do_booking():
    info("Info",".- A\
        ,-... B\
	, -.-. C\
	, -.. D\
	, . E\
	, ..-. F\
	, --. G\
	, .... H\
	, .. I\
	, .--- J\
	, -.- K\
	, .-.. L\
	, -- M\
	, -. N\
	, --- O\
	, .--. P\
	, --.- Q\
	, .-. R\
	, ... S\
	, - T\
	, ..- U\
	, ...- V\
	, .-- W\
	, -..- X\
	, -.-- Y\
	, --.. Z\
	,.---- 1\
	,..--- 2\
	,...-- 3\
	,....- 4\
	,..... 5\
	,-.... 6\
	,--... 7\
	,---.. 8\
	,----. 9\
	,-----0\
	, .-.-.- (.)\
	, --..-- (,)\
	, ..--.. (?)\
	,.----.'\
	, -.-.-- (!)\
	, -..-. (/)\
	, -.--. (\
	, -.--.-)\
	, .-... (&)\
	, ---... (:)\
	, -.-.-.(;)\
	, -...- (=)\
	, .-.-. (+)\
	, -....-(-)\
	, ..--.- (_)\
        , .-..-. (\)\
	, ...-..- ($)\
	, .--.-. (@)\
	, .-.- |AA|\
	, .-.-.|AR|\
	, .-... |AS|\
	, -...- |BT|\
	, -.-.-|CT|\
	, -.--. |KN|\
	, ...-.- |SK|\
	, ...-.|SN|\
	, ...---... |SOS|\
	, --...--  happy face\
	, -.....-  normal face\
	, -.---.-  sad face")
    
book_seats = PushButton(app, command=do_booking, text="Info", grid=[3,2], align="left") 
def do_instrucoes():
    info("instrucões","Press middle to (.)\
                       Press down to (-)\
                       Press right to add space\
                       Press left to select a letter\
                       Press up to show the message\
                       Press up for over 2 sec to make raspberry speak\
                       Press right for over 2 sec to send email\
                       \
                       Press down for over 2 sec to go back to the menu")

book_seats = PushButton(app, command=do_instrucoes, text="Instruções", grid=[3,3], align="left")

my_cat = Picture(app, image="giphy.gif") 
