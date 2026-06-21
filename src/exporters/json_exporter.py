import json
import os
from datetime import datetime


def export_to_json(test_cases, filename=None):
    # Create output folder if it doesn't exist
    os.makedirs("output", exist_ok=True)

    # Auto generate filename with timestamp if not given
    if not filename:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"output/test_cases_{timestamp}.json"

    # Write to JSON file
    with open(filename, "w") as f:
        json.dump(test_cases, f, indent=4)

    print(f"\n✅ Test cases saved to: {filename}")
    return filename