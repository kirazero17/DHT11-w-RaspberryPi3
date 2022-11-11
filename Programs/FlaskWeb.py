#basic imports
import datetime
import time
import pytz

# for Flask web server
from flask import Flask, render_template, request, Response, jsonify,make_response
from turbo_flask import Turbo #Dynamic web
import threading # for BG Update thread
#import DHTRasp #remove the first # of this line
      
# initialization
tzone = pytz.timezone("Asia/Ho_Chi_Minh")      
app = Flask(__name__, template_folder='../templates')
turbo = Turbo(app)

#DHTRasp.init()

def update_load():
    with app.app_context():
        while True:
            time.sleep(1)
            turbo.push(turbo.replace(render_template('Layout/values.html'), 'load'))


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
#    t,humidity=DHTRasp.sensread(DHTRasp.sensorid) #getting the temperature
    templateData = {
       'senid' : 'IDXX',
       'room' : 'Testing Room',
       'time': timeString,
       'temp': 'No data',
       'hum': 'No data',
       'warning': 'None'
       }
    return templateData

# execution
def main():
    app.run(host='0.0.0.0', port=9600, debug=False)

if __name__ == "__main__":
    main()
