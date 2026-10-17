from flask import Flask, request, jsonify
from rent_estimator import estimate_rent
from ai_interrogation_log import record_request
app = Flask(__name__)
@app.route("/")
def home():
    return jsonify({
        "message": "Real Estate AI Rent Estimation API",
        "status": "running"
    })
@app.route("/api/estimate", methods=["POST"])
def estimate():
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return jsonify({
            "error": "Send property details as JSON."
        }), 400
    try:
        bedrooms = int(data["bedrooms"])
        area_sqm = float(data["area_sqm"])
        location = str(data["location"]).strip()
        if bedrooms < 0 or bedrooms > 20:
            raise ValueError("Invalid bedroom count")
        if area_sqm <= 0 or area_sqm > 10000:
            raise ValueError("Invalid floor area")
        if not location or len(location) > 100:
            raise ValueError("Invalid location")
    except (KeyError, TypeError, ValueError):
        return jsonify({
            "error": (
                "Provide valid bedrooms, area_sqm, and location."
            )
        }), 400
    try:
        rent = estimate_rent(bedrooms, area_sqm, location)
        result = {
            "bedrooms": bedrooms,
            "area_sqm": area_sqm,
            "location": location,
            "estimated_monthly_rent_php": rent,
            "status": "prototype",
            "warning": "Estimate uses fictional sample data."
        }
        record_request(
            {
                "bedrooms": bedrooms,
                "area_sqm": area_sqm,
                "location": location
            },
            result,
            "success"
        )
        return jsonify(result)
    except Exception:
        record_request(
            data,
            {"error": "Rent estimation failed."},
            "error"
        )
        return jsonify({
            "error": "Rent estimation failed. Check the server log."
        }), 500
if __name__ == "__main__":
    app.run(debug=True)