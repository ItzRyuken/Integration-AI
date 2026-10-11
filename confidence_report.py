from datetime import datetime
import json
from rent_estimator import estimate_rent, df
def generate_report(bedrooms, area_sqm):
    missing_fields = []
    if bedrooms is None:
        missing_fields.append("bedrooms")
    if area_sqm is None:
        missing_fields.append("area_sqm")
    complete = len(missing_fields) == 0
    report = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "property_inputs": {
            "bedrooms": bedrooms,
            "area_sqm": area_sqm
        },
        "estimated_monthly_rent_php": (
            estimate_rent(bedrooms, area_sqm) if complete else None
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
    result = generate_report(2, 50)
    print(json.dumps(result, indent=4))