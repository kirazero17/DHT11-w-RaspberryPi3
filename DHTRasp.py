#basic imports
import datetime
import pytz
#for DHT11
import board
import adafruit_dht
import psutil

#for Flask web server
from flask import Flask, render_template, request, Response, jsonify,make_response


# We first check if a libgpiod process is running. If yes, we kill it!
for proc in psutil.process_iter():
    if proc.name() == 'libgpiod_pulsein' or proc.name() == 'libgpiod_pulsei':
        proc.kill()
      
#initialization
tzone = pytz.timezone("Asia/Ho_Chi_Minh")      
app = Flask(__name__, template_folder='templates')
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


#for the web
@app.route("/")
def home():
    now = datetime.datetime.now(tzone)
    timeString = now.strftime("%d-%m-%Y %H:%M") #getting the current date and time
    t,humidity=sensread(sensorid) #getting the temperature
    templateData = {
       'room' : 'HELLO!',
       'time': timeString,
       'temp':t,
       'hum':humidity
       }
    return render_template('index.html', **templateData)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
