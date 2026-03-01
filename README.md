# 🚀 AI-Powered Job Application Automation Bot

A Python-based intelligent automation system that applies to jobs automatically using Selenium and AI-generated responses.

This project demonstrates advanced browser automation, multi-step form handling, dynamic DOM interaction, and AI integration for intelligent question answering.

> ⚠️ This project is built strictly for educational and learning purposes.

---

## 📌 Overview

Job applications often require repetitive manual effort — opening listings, clicking “Easy Apply”, filling forms, answering screening questions, and uploading resumes.

This system automates the entire workflow:

```
Job Search → Easy Apply Detection → Multi-Step Form Fill → 
AI Question Answering → Submit → Close Tab → Repeat
```

The bot intelligently interacts with dynamic job application pages and uses AI to generate contextual answers to screening questions.

---

## 🧠 Key Features

### ✔ Intelligent Job Detection

* Loads configurable job search URL
* Scrolls dynamically to load listings
* Filters only “Easy Apply” jobs
* Opens job cards safely in new tabs

### ✔ Multi-Step Application Automation

* Auto-fills contact information
* Handles resume step
* Fills experience details
* Navigates multi-page application flows

### ✔ AI-Powered Screening Question Engine

* Dynamically detects question containers
* Supports:

  * Text inputs
  * Textarea responses
  * Dropdown selections
* Generates contextual answers using GPT API
* Automatically respects character limits

### ✔ Persistent Browser Session

* Uses `undetected_chromedriver`
* Saves Chrome profile locally
* Prevents repeated login
* Reduces bot detection risk

### ✔ Structured Error Logging

Each exception logs:

* Timestamp
* Error type
* File name
* Function name
* Line number

Example:

```
Timestamp: 2026-01-01 10:22:33 |
Error_Message: Element not found |
Function: apply_to_jobs |
File_Name: main.py |
Line_No: 120
```

### ✔ Centralized Configuration

All runtime configuration is handled via `.env` file.

No hardcoded credentials.

---

## 🏗 System Architecture

```
main.py
│
├── Driver Initialization
├── Job Fetch & Filter
├── Apply Loop
│
├── form_fill_action.py 
│   ├── Contact Info Fill
│   ├── Resume Step
│   └── Experience Handling
│
├── AI_Action.py
│   ├── Question Detection
│   ├── Input Type Identification
│   └── GPT Answer Handling
│
├── gpt_main.py
│   └── OpenAI API Communication
│
└── utils/
    ├── driver.py
    └── print_exception.py
```

---

## 🔐 First-Time Setup Requirement

When running the bot for the first time:

1. The browser will open.
2. You must manually log in.
3. Upload your resume manually once.

Why?

The system uses a persistent Chrome profile.
Once logged in, your session is saved locally.

From the next run onward:

* The script automatically opens your logged-in profile.
* No need to log in again (unless logged out manually).

---

## ⚙️ Environment Configuration

Create a `.env` file:

```env
gpt_API_kye=sk-XXXXXXXXXXXXXXXX
gpt_Prompt_id=1234567788

JOB_SEARCH_URL=https://www.glassdoor.co.in/Job/index.htm
WAIT_BETWEEN_APPS=5
MAX_APPLICATIONS=5

POSTAL_CODE=560001
CITY=Bangalore, Karnataka
JOB_TITLE=Software Engineer
COMPANY=XYZ
```

⚠️ Never commit real API keys.

---

## ▶️ Installation & Usage

### 1️⃣ Clone Repository

```bash
git clone https://github.com/junedkhan9310/Job-Application-automate.git
cd Job-Application-automate
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Bot

```bash
python main.py
```

---

## 🛠 Tech Stack

* Python
* Selenium
* Undetected ChromeDriver
* OpenAI API
* dotenv

---

## 📈 Future Improvements

* Async / parallel job processing
* Retry logic for failed submissions
* Resume auto-selection intelligence
* GUI dashboard
* Database tracking of applications
* Human-like random delay modeling
* CAPTCHA detection handling
* Smart job filtering (salary / role / location)

---

## 🛡 Disclaimer

This project is built strictly for:

* Educational purposes
* Learning browser automation
* Demonstrating AI-assisted workflow automation
* Research and experimentation

Users are fully responsible for complying with:

* Website terms of service
* Platform usage policies
* Ethical automation practices

The author does not promote spam, misuse, or violation of any platform rules.

---

## 👨‍💻 Author

**Juned Khan**
AI & Automation Developer
Final Year — Artificial Intelligence & Data Science

Focused on:

* AI-driven automation
* Intelligent workflow systems
* Real-world applied machine learning

---