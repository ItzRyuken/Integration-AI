from flask import Flask, request, jsonify
from rent_estimator import estimate_rent
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
        return jsonify({"error": "Send property details as JSON."}), 400
    try:
        bedrooms = int(data["bedrooms"])
        area_sqm = float(data["area_sqm"])
        if bedrooms < 0 or bedrooms > 20:
            raise ValueError()
        if area_sqm <= 0 or area_sqm > 10000:
            raise ValueError()
    except (KeyError, TypeError, ValueError):
        return jsonify({
            "error": "Provide valid bedrooms and area_sqm values."
        }), 400
    rent = estimate_rent(bedrooms, area_sqm)
    return jsonify({
        "bedrooms": bedrooms,
        "area_sqm": area_sqm,
        "estimated_monthly_rent_php": rent,
        "status": "prototype",
        "warning": "Estimate uses fictional sample data."
    })
if __name__ == "__main__":
    app.run(debug=True)