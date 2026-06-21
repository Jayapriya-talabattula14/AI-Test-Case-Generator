import csv
import os
from datetime import datetime


def export_to_csv(test_cases, filename=None):
    # Create output folder if it doesn't exist
    os.makedirs("output", exist_ok=True)

    # Auto generate filename with timestamp
    if not filename:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"output/test_cases_{timestamp}.csv"

    # Write to CSV file
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "id", "title", "type",
            "steps", "expected_result", "why"
        ])
        writer.writeheader()
        writer.writerows(test_cases)

    print(f"✅ Test cases saved to: {filename}")
    return filename