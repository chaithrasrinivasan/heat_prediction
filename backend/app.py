from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load model
try:
    model = pickle.load(open(r"D:\Project\heat_prediction\models\heat_model.pkl", "rb"))
    print("Model loaded")
except Exception as e:
    print("Model loading error:", e)
    model = None


@app.route("/")
def home():
    return "Server is running"


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json
        print("Incoming data:", data)

        # Extract values directly
        temp = data.get("temperature")
        hum = data.get("humidity")

        print("Temp:", temp, "Humidity:", hum)

        # Convert to float
        temp = float(temp)
        hum = float(hum)

        # Create input array
        input_data = np.array([[temp, hum]])

        print("Model input:", input_data)

        # Predict
        result = model.predict(input_data)

        print("Prediction:", result)

        return jsonify({"prediction": str(result[0])})

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run(debug=True)