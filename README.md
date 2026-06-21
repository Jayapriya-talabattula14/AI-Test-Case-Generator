# 🤖 AI Test Case Generator

> Generate smart QA test cases from user stories in seconds using AI.

## ✨ What It Does
Automatically generates **5 structured test cases** including:
- ✅ Positive scenarios
- ❌ Negative scenarios
- ⚠️ Edge cases
- 🔒 Security scenarios

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Groq](https://img.shields.io/badge/API-Groq-orange)
![LLaMA](https://img.shields.io/badge/Model-LLaMA3.3-purple)

---

## 🚀 Quick Start

```bash
# 1. Clone
git clone https://github.com/Jayapriya-talabattula14/AI-Test-Case-Generator.git

# 2. Install
pip install -r requirements.txt

# 3. Add API key in .env
GROQ_API_KEY=your_key_here

# 4. Run
python src/cli.py
```

Get free API key at 👉 https://console.groq.com

---

## 📊 Sample Output

| ID | Title | Type | Expected Result |
|----|-------|------|----------------|
| TC001 | Successful Login | ✅ Positive | User redirected to dashboard |
| TC002 | Invalid Password | ❌ Negative | Error message displayed |
| TC003 | Empty Fields | ⚠️ Edge Case | Validation errors shown |
| TC004 | SQL Injection | 🔒 Security | Attack blocked |

---

## 📁 Output Formats

- `output/test_cases_timestamp.json`
- `output/test_cases_timestamp.csv`

---

## 👩‍💻 Author

**Jayapriya Talabattula** — QA Engineer transitioning to SDET

[![GitHub](https://img.shields.io/badge/GitHub-Jayapriya-black)](https://github.com/Jayapriya-talabattula14)
