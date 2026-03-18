from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

model = pickle.load(open("models/heat_model.pkl","rb"))

labels = {
    0: "Low",
    1: "Medium",
    2: "High"
}

@app.route("/predict_heat", methods=["POST"])
def predict_heat():

    data = request.json

    sample = pd.DataFrame([[

        data["temperature_2m_max"],
        data["temperature_2m_min"],
        data["precipitation_sum"],
        data["wind_speed_10m_max"]

    ]], columns=[
        "temperature_2m_max",
        "temperature_2m_min",
        "precipitation_sum",
        "wind_speed_10m_max"
    ])

    prediction = model.predict(sample)[0]

    return jsonify({"heat_risk": labels[prediction]})


@app.route("/")
def home():
    return "Heat Risk Prediction API is Running"


if __name__ == "__main__":
    app.run(debug=True)