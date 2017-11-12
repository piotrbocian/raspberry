import sys
import requests
from time import sleep
import Adafruit_DHT as dht
from gpiozero import CPUTemperature


while True:
    h,t = dht.read_retry(dht.DHT22, 2)
    print 'Indoor Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(t, h)
    cpu = CPUTemperature()
    print(cpu.temperature)
    try:
        r = requests.get("https://api.thingspeak.com/update?api_key=0WIZJD43UXQF71TQ&field1={0:0.1f}&field2={1:0.1f}&field3={2}".format(t, h, cpu.temperature))
        print(r)
    except requests.exceptions.ConnectionError as error:
        print(error)
    except:
        print("Unexpected error:", sys.exc_info()[0])
        
    sleep(300)
