#basic imports
import datetime
import time
import pytz

# for Flask web server
from flask import Flask, render_template, request, Response, jsonify,make_response
from turbo_flask import Turbo #Dynamic web
import threading # for BG Update thread
#import DHTRasp.py
      
# initialization
tzone = pytz.timezone("Asia/Ho_Chi_Minh")      
app = Flask(__name__, template_folder='templates')
turbo = Turbo(app)

def update_load():
    with app.app_context():
        while True:
            time.sleep(1)
            turbo.push(turbo.replace(render_template('values.html'), 'load'))


# for the web
@app.route("/")
def home():
    return render_template('index.html')

# update thread
@app.before_first_request
def before_first_request():
    threading.Thread(target=update_load).start()
    
@app.context_processor
def inject_load():
    now = datetime.datetime.now(tzone)
    timeString = now.strftime("%d-%m-%Y %H:%M:%S") # getting the current date and time
#    t,humidity=sensread(sensorid) #getting the temperature
    templateData = {
       'senid' : 'IDXX',
       'room' : 'Testing Room',
       'time': timeString,
       'temp': 'No data',
       'hum': 'No data'
       }
    return templateData

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=90)
