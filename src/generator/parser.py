import json


def parse_response(ai_response):
    # Split the response into individual test cases
    test_cases = []

    # Split by "Test Case ID" to separate each test case
    raw_cases = ai_response.split("- Test Case ID:")

    # First item is empty, skip it
    for i, case in enumerate(raw_cases[1:], 1):
        lines = case.strip().split("\n")

        test_case = {
            "id": f"TC{i:03d}",
            "title": "",
            "type": "",
            "steps": "",
            "expected_result": "",
            "why": ""
        }

        for line in lines:
            line = line.strip()
            if line.startswith("- Title:"):
                test_case["title"] = line.replace("- Title:", "").strip()
            elif line.startswith("- Type:"):
                test_case["type"] = line.replace("- Type:", "").strip()
            elif line.startswith("- Steps:"):
                test_case["steps"] = line.replace("- Steps:", "").strip()
            elif line.startswith("- Expected Result:"):
                test_case["expected_result"] = line.replace("- Expected Result:", "").strip()
            elif line.startswith("- Why this test:"):
                test_case["why"] = line.replace("- Why this test:", "").strip()

        test_cases.append(test_case)

    return test_cases


def display_test_cases(test_cases):
    # Print test cases nicely in terminal
    print("\n" + "=" * 60)
    print(f"Generated {len(test_cases)} Test Cases")
    print("=" * 60)

    for tc in test_cases:
        print(f"\n📋 {tc['id']} — {tc['title']}")
        print(f"   Type: {tc['type']}")
        print(f"   Steps: {tc['steps']}")
        print(f"   Expected: {tc['expected_result']}")
        print(f"   Why: {tc['why']}")
        print("-" * 60)