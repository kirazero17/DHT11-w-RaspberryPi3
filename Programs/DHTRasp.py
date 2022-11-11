# for DHT11
import board
import adafruit_dht
import psutil

# We first check if a libgpiod process is running. If yes, we kill it!
def init():
    for proc in psutil.process_iter():
        if proc.name() == 'libgpiod_pulsein' or proc.name() == 'libgpiod_pulsei':
            proc.kill()

sensorid = adafruit_dht.DHT11(board.D23)  #Connect output to GPIO23


def sensread(sensor):  
     try:
         temp = str(sensor.temperature)
         humidity = str(sensor.humidity)
         print("Temperature: {}*C   Humidity: {}% ".format(temp, humidity))
         return temp, humidity
     except RuntimeError as error:
         temp = 'NaN'
         humidity = 'NaN'
         print(error.args[0])
         return temp, humidity
     except Exception as error:
         print ('Error: '+str(e))
         GPIO.cleanup()