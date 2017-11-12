from gpiozero import MotionSensor
import time

pir = MotionSensor(14)

while True:
        pir.wait_for_motion()
        time1 = time.time()
        print("You moved")
        pir.wait_for_no_motion()
        time2 = time.time()
        print("------")
        print(time2 - time1)
