#basic imports
import datetime
import time
import pytz

# for Flask web server
from flask import Flask, render_template, request, Response, jsonify,make_response
from turbo_flask import Turbo #Dynamic web
import threading # for BG Update thread
import DHTRasp as DHT  #remove the first # of this line
      
# initialization
tzone = pytz.timezone("Asia/Ho_Chi_Minh")      
app = Flask(__name__, template_folder='../templates')
turbo = Turbo(app)


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
    t,humidity=DHT.snsrd() #getting the temperature
    if int(t) > 40 or float(humidity) > 70.:
        warning = "Yes"
    else:
        warning = "No"
    
    if t < -273:
        t = 'NaN'
    if humidity < 0:
        humidity = 'NaN'
    
    templateData = {
       'senid' : '1234',
       'room' : 'Test Room',
       'time': timeString,
       'temp': str(t),
       'hum': str(humidity),
       'warning': warning
       }
    return templateData

# execution
def main():
    app.run(host='0.0.0.0', port=9600, debug=False)

if __name__ == "__main__":
    main()
