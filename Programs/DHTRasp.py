# for DHT11
import board
import adafruit_dht as dht
import psutil

def snsrd():
    # We first check if a libgpiod process is running. If yes, we kill it!
    for proc in psutil.process_iter():
        if proc.name() == 'libgpiod_pulsein' or proc.name() == 'libgpiod_pulsei':
            proc.kill()
    dhtdev = dht.DHT11(board.D22, True)
    try:
        temp = dhtdev.temperature #Connect output to GPIO22
        humidity = dhtdev.humidity
        print("Temperature: {}*C   Humidity: {}% ".format(temp, humidity))
        dhtdev.exit()
        return temp, humidity
    except RuntimeError as error:
        temp = -1
        humidity = -274
        print(error.args[0])
        dhtdev.exit()
        return temp, humidity 
    except Exception as error:
        temp = -1
        humidity = -274
        print ('Error: '+ str(error))
        dhtdev.exit()
        return temp, humidity 
         
if __name__ == "__main__":
    snsrd()
