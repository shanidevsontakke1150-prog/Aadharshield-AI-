import random

def check_for_fraud(aadhaar_id, location, device, service):
    suspicious_locations = ["unknown", "foreign", "darknet"]
    risky_services = ["bank", "sim", "loan"]

    risk_score = 0
    reasons = []

    if location.lower() in suspicious_locations:
        risk_score += 40
        reasons.append("Suspicious location")

    if service.lower() in risky_services:
        risk_score += 30
        reasons.append("High-risk service")

    if random.random() > 0.7:
        risk_score += 30
        reasons.append("Unusual activity pattern")

    if risk_score >= 60:
        return "HIGH", ", ".join(reasons)
    elif risk_score >= 30:
        return "MEDIUM", ", ".join(reasons)
    else:
        return "LOW", "Normal behavior"
