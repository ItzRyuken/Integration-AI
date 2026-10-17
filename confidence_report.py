from datetime import datetime
import json
from rent_estimator import estimate_rent, df, mae
def generate_report(bedrooms, area_sqm, location):
    missing_fields = []
    if bedrooms is None:
        missing_fields.append("bedrooms")
    if area_sqm is None:
        missing_fields.append("area_sqm")
    if not location:
        missing_fields.append("location")
    complete = len(missing_fields) == 0
    report = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
                "property_inputs": {
            "model_version": "prototype-1.0",
            "test_mae_php": round(float(mae), 2),
            "confidence_note": "No calibrated prediction confidence is available. The model uses a small fictional dataset.",
            "bedrooms": bedrooms,
            "area_sqm": area_sqm,
            "location": location
        },
        "estimated_monthly_rent_php": (
        estimate_rent(bedrooms, area_sqm, location) if complete else None
        ),
        "input_completeness": (
            "Complete" if complete else "Incomplete"
        ),
        "missing_fields": missing_fields,
        "reliability_note": (
            "This is a prototype using fictional sample data. "
            "Input completeness is not a measure of prediction accuracy."
        )
    }
    return report
if __name__ == "__main__":
    result = generate_report(2, 50, "Cainta")
    print(json.dumps(result, indent=4))