import time
import random
import requests

API_URL = "https://<TUO_FASTAPI_URL>/iot-data"

def generate_data():
    return {
        "id": random.randint(1, 100),
        "temperature": round(random.uniform(18.0, 26.0), 2),
        "humidity": round(random.uniform(40.0, 70.0), 2),
        "gps": {
            "lat": 43.7167,
            "lon": 10.4000
        }
    }

while True:
    data = generate_data()
    print("Sending data:", data)
    try:
        requests.post(API_URL, json=data)
    except Exception as e:
        print("Error sending data:", e)
    time.sleep(10)
