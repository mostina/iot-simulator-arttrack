import os
import time
import random
import requests
from datetime import datetime, timezone, timedelta


# 🔗 URL  endpoint FastAPI 
API_URL = os.environ.get("API_URL") 

# 🔹 ArtWorks ID (the same as the ones in artworks db)
ARTWORK_IDS = [
    "OP001", "OP002", "OP003", "OP004", "OP005",
    "OP006", "OP007", "OP008", "OP009", "OP010",
    "OP011", "OP012", "OP013", "OP014", "OP015",
    "OP016", "OP017", "OP018", "OP019", "OP020",
    "OP021", "OP022", "OP023", "OP024", "OP025",
    "OP026", "OP027", "OP028", "OP029", "OP030"
]

def generate_data(artwork_id):
    cet = timezone(timedelta(hours=1))  # CET timezone (UTC+1)
    now_cet = datetime.now(cet).strftime("%d/%m/%Y %H:%M")

    return {
        "id": artwork_id,  
        "latitude": round(43.5 + random.uniform(-0.5, 0.5), 6),
        "longitude": round(10.4 + random.uniform(-0.5, 0.5), 6),
        "temperature": round(random.uniform(18.0, 26.0), 2),
        "humidity": round(random.uniform(40.0, 70.0), 2),
        "timestamp": now_cet
    }

def send_data(data):
    """Send data to FastAPI."""
    try:
        response = requests.post(API_URL, json=data, timeout=5)
        if response.status_code == 200:
            print(f"Updated {data['id']} successfully.")
        else:
            print(f" Server response {response.status_code}: {response.text}")
    except Exception as e:
        print("Error sending data:", e)

if __name__ == "__main__":
    print(" IoT simulator started. Sending data every 60 seconds...")
    for artwork_id in ARTWORK_IDS:
            data = generate_data(artwork_id)
            print("Sending:", data)
            send_data(data)
            time.sleep(5)  #  delay between artworks
       
