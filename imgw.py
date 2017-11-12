import sys
import requests
from time import sleep

while True:
    try:
        gdansk_imgw = requests.get("https://danepubliczne.imgw.pl/api/data/synop/station/gdansk")
        gdansk_json = gdansk_imgw.json()
        gdansk_t = gdansk_json['temperatura']
        gdansk_h = gdansk_json['wilgotnosc_wzgledna']
        print('Gdansk Temp='+gdansk_t+'*C  Humidity='+gdansk_h+'%')
        r = requests.get("https://api.thingspeak.com/update?api_key=0WIZJD43UXQF71TQ&field4="+gdansk_t+"&field5="+gdansk_h)
        print(r)
    except requests.exceptions.ConnectionError as error:
        print(error)
    except:
        print("Unexpected error:", sys.exc_info()[0])
        
        
    sleep(330)
