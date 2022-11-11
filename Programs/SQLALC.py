import datetime
import time
import pytz

import requests
import json
from flask import Flask, request, render_template, session, jsonify

#import DHTRasp

# main function to call
def main():
#    t,humidity=DHTRasp.sensread(DHTRasp.sensorid)
    tzone = pytz.timezone("Asia/Ho_Chi_Minh")
    url = "http://"
    data = {}
    data["sensor_id"] = "DHT01"
    data["room_id"] = "STR01"
    
    headers = {'Content-Type': 'application/json'}
    payload = {}
    while True:
        data["temperature"] = '0'
        data["humidity"] = '0'
        data["date"] = datetime.datetime.now(tzone).strftime("%d-%m-%Y %H:%M:%S")
        payload = json.dumps(data)
        
        response = requests.request("POST", url, headers=headers, data=payload)
        time.sleep(5)
    
    
if __name__ == "__main__":
    main()
