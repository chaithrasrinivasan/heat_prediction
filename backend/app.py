print("🔥 FINAL BACKEND RUNNING")

from flask import Flask, request, jsonify
import pandas as pd

from backend.weather import get_weather
from backend.model_loader import model

app = Flask(__name__)


# 🔹 Heat labels
labels = {
    0: "Low",
    1: "Medium",
    2: "High"
}


# 🔹 Heat advice
heat_advice = {
    "Low": {
        "clothing": "Wear light casual clothes.",
        "outdoor": "Safe for outdoor activities.",
        "hydration": "Drink water regularly."
    },
    "Medium": {
        "clothing": "Wear cotton clothes and sunscreen.",
        "outdoor": "Avoid 12–3 PM sun.",
        "hydration": "Drink water frequently."
    },
    "High": {
        "clothing": "Wear caps and breathable clothes.",
        "outdoor": "Avoid 11 AM – 4 PM.",
        "hydration": "Drink water every 20–30 mins."
    }
}


# 🔹 Climate logic
def climate_solutions(temp):

    if temp <= 0:
        return "Freezing", {"advice": "Wear heavy winter gear"}
    elif temp <= 10:
        return "Cold", {"advice": "Wear jackets"}
    elif temp <= 25:
        return "Moderate", {"advice": "Comfortable weather"}
    elif temp <= 35:
        return "Warm", {"advice": "Use sunscreen"}
    else:
        return "Hot / Heatwave", {
            "clothing": "Wear light breathable clothes",
            "hydration": "Drink water frequently",
            "safety": "Stay indoors during peak heat"
        }


# 🏠 HOME
@app.route("/")
def home():
    return "Backend Running Successfully"


# 🔥 MAIN API
@app.route("/api/live", methods=["POST"])
def predict_heat():

    try:
        data = request.get_json()

        lat = data.get("lat")
        lon = data.get("lon")

        if lat is None or lon is None:
            return jsonify({"error": "lat and lon required"}), 400

        # 🌦️ Get weather
        temp, humidity, pressure, wind = get_weather(lat, lon)

        # Convert to model format
        temp_max = temp + 1
        temp_min = temp - 1
        precip = 0

        # DataFrame input
        sample = pd.DataFrame([[temp_max, temp_min, precip, wind]], columns=[
            "temperature_2m_max",
            "temperature_2m_min",
            "precipitation_sum",
            "wind_speed_10m_max"
        ])

        # Predict
        prediction = model.predict(sample)[0]
        heat_risk = labels[prediction]

        avg_temp = (temp_max + temp_min) / 2
        climate, climate_advice = climate_solutions(avg_temp)

        return jsonify({
            "temperature": temp,
            "humidity": humidity,
            "heat_risk": heat_risk,
            "heat_advice": heat_advice[heat_risk],
            "climate_type": climate,
            "climate_solutions": climate_advice
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# 🗺️ HEATMAP API (Member 4)
@app.route("/api/heatmap/<city>")
def heatmap(city):

    data = [
        {"lat": 13.085, "lon": 80.210, "risk": "High"},
        {"lat": 13.041, "lon": 80.234, "risk": "Medium"},
        {"lat": 12.981, "lon": 80.220, "risk": "Low"}
    ]

    return jsonify(data)


# 💬 CHATBOT API (Member 4)
@app.route("/api/chat", methods=["POST"])
def chat():

    msg = request.json.get("message", "").lower()

    if "heat" in msg:
        return jsonify({"reply": "Heat is high. Stay hydrated and avoid sun."})

    if "safe time" in msg:
        return jsonify({"reply": "Avoid outdoor activity between 11 AM and 4 PM."})

    return jsonify({"reply": "Ask about heat, safety, or climate."})


# ▶️ RUN
if __name__ == "__main__":
    app.run(debug=True)