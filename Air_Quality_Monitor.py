import RPi.GPIO as GPIO 
from time import sleep
import Adafruit_DHT 
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN)
DHT_SENSOR = Adafruit_DHT.DHT22 
DHT_PIN = 4 
humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN) 

print("AIR QUALITY MONITOR\n RASPBERRY PI\n" ) 
sleep(3) 

def main1(): 
    if GPIO.input(17): 
        print(" GAS SENSOR\n COOL ENVIRONMENT\n") 
    else: 
        print(" GAS SENSOR\n GAS DETECTED\n") 
    sleep(3) 
    
def main2():
    if humidity is not None and temperature is not None: 
        print(" HUMIDITY SENSOR\n TEMP={0:0.1f}*C HUM.{1:0.1f}%\n".format(temperature, humidity)) 
    else: 
        print(" HUMIDITY SENSOR\n Failed to retrieve data\n") 
    sleep(3) 

def main(): 
    while True: 
        main1() , main2() 

main() 