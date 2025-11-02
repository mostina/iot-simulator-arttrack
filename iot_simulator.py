import time
import random
import requests
from datetime import datetime


# 🔗 URL del tuo endpoint FastAPI (cambialo con il tuo vero indirizzo)
API_URL = "https://museofastapi.onrender.com/iot-data/update"

# 🔹 Lista delle opere (stessi ID della collezione artworks)
ARTWORK_IDS = [
    "OP001", "OP002", "OP003", "OP004", "OP005",
    "OP006", "OP007", "OP008", "OP009", "OP010"
]

def generate_data(artwork_id):
    return {
        "id": artwork_id,  # <- qui invece di "_id"
        "latitude": round(43.5 + random.uniform(-0.5, 0.5), 6),
        "longitude": round(10.4 + random.uniform(-0.5, 0.5), 6),
        "temperature": round(random.uniform(18.0, 26.0), 2),
        "humidity": round(random.uniform(40.0, 70.0), 2),
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }

def send_data(data):
    """Invia i dati al server FastAPI."""
    try:
        response = requests.post(API_URL, json=data, timeout=5)
        if response.status_code == 200:
            print(f"✅ Updated {data['_id']} successfully.")
        else:
            print(f"⚠️ Server response {response.status_code}: {response.text}")
    except Exception as e:
        print("❌ Error sending data:", e)

if __name__ == "__main__":
    print("🚀 IoT simulator started. Sending data every 10 seconds...")
    while True:
        for artwork_id in ARTWORK_IDS:
            data = generate_data(artwork_id)
            print("📡 Sending:", data)
            send_data(data)
            time.sleep(1)  # piccolo delay tra un’opera e l’altra
        time.sleep(10)  # aspetta 10s prima del prossimo ciclo
