from traffic_light import TrafficLight
import time
import RPi.GPIO as GPIO


# iniciando Objetos semaforo

traffic_lights = [ TrafficLight(7,9,11), TrafficLight(8,10,12) ]

# iniciando Pines

GPIO.setmode(GPIO.BOARD)


for trafl in traffic_lights:
    for pin in trafl.states:
        GPIO.setup(pin, GPIO.OUT)




# variables que serviran para el cambio de estados
tl = 0

a = 2
b = 0



for i in range(0,3):

    GPIO.output(7, True)
    time.sleep(1)
    GPIO.output(7, False)
    time.sleep(1)

    if tl == 0 and b < 2:
        b += 1
        a -= 1
    elif b >= 2:
        tl = 1
    
    if tl == 1 and a < 2:
        a += 1
        b -= 1
    elif a >= 2:
        tl = 0
        a = 1
        b = 1

GPIO.cleanup()