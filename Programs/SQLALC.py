import datetime
import time
import pytz
import requests
import json

import DHTRasp as DHT

# main function to call
def main():
    tzone = pytz.timezone("Asia/Ho_Chi_Minh")
    url = "http://ec2-18-140-69-222.ap-southeast-1.compute.amazonaws.com/api/sensor"
    
    data = {}
   
    headers = {'Content-Type': 'application/json'}
    payload = {}
    while True:
        data["sensor_id"] = "DHT01"
        data["room_id"] = "STR01"
    
        data["temperature"], data["humidity"] = DHT.snsrd()
        data["date"] = datetime.datetime.now(tzone).strftime("%Y-%m-%d %H:%M:%S")
        payload = json.dumps(data)
        
        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
        # print(data)
        print("\n")
        time.sleep(5)
    
    
if __name__ == "__main__":
    main()
