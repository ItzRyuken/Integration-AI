import csv
from datetime import datetime
from pathlib import Path
LOG_FILE = Path(__file__).parent / "ai_interrogation_log.csv"
def record_request(inputs, output, status):
    file_exists = LOG_FILE.exists()
    with LOG_FILE.open("a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow([
                "timestamp",
                "inputs",
                "output",
                "status"
            ])
        writer.writerow([
            datetime.now().isoformat(timespec="seconds"),
            str(inputs),
            str(output),
            status
        ])
if __name__ == "__main__":
    record_request(
        {"bedrooms": 2, "area_sqm": 50},
        {"estimated_rent_php": 9815},
        "prototype_test"
    )
    print(f"Log saved to: {LOG_FILE}")