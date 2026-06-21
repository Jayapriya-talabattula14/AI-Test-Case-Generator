import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.generator.claude_client import ask_ai
from src.generator.prompt_builder import build_prompt
from src.generator.parser import parse_response, display_test_cases
from src.exporters.json_exporter import export_to_json
from src.exporters.csv_exporter import export_to_csv

def main():
    print("="*60)
    print("  AI Test Case Generator")
    print("="*60)

    user_story = input("\nEnter your user story:\n> ")
    domain = input("\nEnter domain (login/payment/api/general):\n> ")

    print("\n⏳ Generating test cases, please wait...")

    # Generate
    prompt = build_prompt(user_story, domain)
    ai_response = ask_ai(prompt)
    test_cases = parse_response(ai_response)

    # Display
    display_test_cases(test_cases)

    # Ask user what to export
    print("\nExport options:")
    print("1. JSON")
    print("2. CSV")
    print("3. Both")
    print("4. Skip")

    choice = input("\nYour choice (1/2/3/4):\n> ")

    if choice == "1":
        export_to_json(test_cases)
    elif choice == "2":
        export_to_csv(test_cases)
    elif choice == "3":
        export_to_json(test_cases)
        export_to_csv(test_cases)
    else:
        print("\nSkipping export.")

    print("\n✅ Done!")

if __name__ == "__main__":
    main()