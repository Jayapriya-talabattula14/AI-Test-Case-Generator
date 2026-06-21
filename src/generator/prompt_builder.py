def build_prompt(user_story, domain="general"):
    # This builds the question we send to Gemini
    prompt = f"""
You are a senior QA engineer with 10 years of experience.

Given this user story:
\"{user_story}\"

Generate 5 test cases in this exact format for each:
- Test Case ID: TC001
- Title: (short title)
- Type: (Positive / Negative / Edge Case)
- Steps: (step by step)
- Expected Result: (what should happen)
- Why this test: (explain why this is important)

Domain context: {domain}

Be thorough and think like an experienced QA engineer.
"""
    return prompt