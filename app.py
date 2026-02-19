from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

zones = ["Zone A", "Zone B", "Zone C", "Zone D", "Zone E", "Zone F", "Zone G", "Zone H"]

def generate_data():
    data = []
    for zone in zones:
        pressure = round(random.uniform(0.8, 3.0), 2)
        flow = round(random.uniform(20, 120), 2)

        if pressure < 1.2:
            status = "CRITICAL"
        elif pressure < 1.8:
            status = "WARNING"
        else:
            status = "NORMAL"

        data.append({
            "zone": zone,
            "pressure": pressure,
            "flow": flow,
            "status": status
        })
    return data

@app.route("/")
def dashboard():
    return render_template("dashboard.html")

@app.route("/data")
def data():
    return jsonify(generate_data())

if __name__ == "__main__":
    app.run(debug=True)
