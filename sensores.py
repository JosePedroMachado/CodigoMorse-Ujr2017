from sense_hat import SenseHat
sense = SenseHat()

def sensortype():

    t = sense.get_temperature()
    p = sense.get_pressure()
    h = sense.get_humidity()

    t = round(t, 1)
    p = round(p, 1)
    h = round(h, 1)

    msg = "Temperatura = {0}, Pressao = {1}, Humidade - {2}".format(t, p, h)
    sense.show_message(msg, scroll_speed=0.04)




