from gpiozero import RGBLED
from signal import pause
from random import randint
from time import sleep

led = RGBLED(red=20, green=19, blue=26, active_high=False)

led.red = randint(1,99)/float(100)
led.green = randint(1,99)/float(100)
led.blue = randint(1,99)/float(100)
    
while True:

    new_red = randint(1,99)/float(100)
    new_green = randint(1,99)/float(100)
    new_blue = randint(1,99)/float(100)

    new_red *= new_red;
    new_green *= new_green;
    new_blue *= new_blue;

    step_red = (new_red - led.red) / 10;
    step_green = (new_green - led.green) / 10;
    step_blue = (new_blue - led.blue) / 10;

    #print("[{}] [{}] [{}]".format(step_red, step_green, step_blue))
    
    for n in range(10):
        led.red += step_red;
        led.green += step_green;
        led.blue += step_blue;
        #print("{} {} {}".format(led.red, led.green, led.blue))
        sleep(0.1)


    
