from flask import Flask, request, jsonify
from flask_cors import CORS
from ai_engine import check_for_fraud
from database import log_event

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "AadhaarShield AI Backend is Running"

@app.route("/check", methods=["POST"])
def check():
    data = request.json or {}

    aadhaar_id = data.get("aadhaar_id", "unknown")
    location = data.get("location", "unknown")
    device = data.get("device", "unknown")
    service = data.get("service", "unknown")

    risk, reason = check_for_fraud(aadhaar_id, location, device, service)

    log_event(aadhaar_id, location, device, service, risk, reason)

    return jsonify({
        "risk": risk,
        "reason": reason
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
