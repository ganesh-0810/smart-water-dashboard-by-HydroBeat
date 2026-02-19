from flask import Flask, render_template, jsonify
import random
import datetime

app = Flask(__name__)

zones_data = [
    {"zone": "Zone A", "area": "Pandharpur", "elevation": "Low"},
    {"zone": "Zone B", "area": "Barshi", "elevation": "Mid"},
    {"zone": "Zone C", "area": "Akkalkot", "elevation": "High"},
    {"zone": "Zone D", "area": "Mangalwedha", "elevation": "Low"},
    {"zone": "Zone E", "area": "Sangola", "elevation": "Mid"},
    {"zone": "Zone F", "area": "Malshiras", "elevation": "High"},
    {"zone": "Zone G", "area": "Mohol", "elevation": "Low"},
    {"zone": "Zone H", "area": "Karmala", "elevation": "Mid"},
]

workers = ["Ramesh", "Suresh", "Anil", "Prakash", "Vijay", "Karthik"]

daily_consumption_tracker = {z["zone"]: 0 for z in zones_data}

def generate_data():
    zones_output = []
    total_water_today = 0
    critical_count = 0
    alerts = []

    for z in zones_data:
        pressure = round(random.uniform(0.8, 3.0), 2)
        flow = round(random.uniform(20, 120), 2)
        consumption_hour = round(flow * 60, 2)  # L/hour simulation

        daily_consumption_tracker[z["zone"]] += consumption_hour
        daily_kl = round(daily_consumption_tracker[z["zone"]] / 1000, 2)

        if pressure < 1.2:
            status = "CRITICAL"
            critical_count += 1
            alerts.append(f"{z['zone']} - Low Pressure Detected")
        elif pressure < 1.8:
            status = "WARNING"
        else:
            status = "NORMAL"

        leak = "YES" if random.random() < 0.1 else "NO"

        zones_output.append({
            "zone": z["zone"],
            "area": z["area"],
            "elevation": z["elevation"],
            "pressure": pressure,
            "flow": flow,
            "consumption_hour": consumption_hour,
            "daily_kl": daily_kl,
            "status": status,
            "leak": leak,
            "worker": random.choice(workers),
            "worker_status": random.choice(["On Site", "Traveling", "Monitoring"])
        })

        total_water_today += daily_kl

    return {
        "zones": zones_output,
        "total_zones": len(zones_data),
        "total_water_today": round(total_water_today, 2),
        "critical_count": critical_count,
        "alerts": alerts
    }

@app.route("/")
def dashboard():
    return render_template("dashboard.html")

@app.route("/data")
def data():
    return jsonify(generate_data())

if __name__ == "__main__":
    app.run(debug=True)
