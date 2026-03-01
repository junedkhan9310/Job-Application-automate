# 🚀 AI Job Application Automation Bot

An AI-powered Python automation system that automatically applies to jobs by handling multi-step application forms, answering screening questions using AI, and submitting applications with minimal manual effort.

This project combines **Selenium automation + AI-assisted decision making** to simulate a realistic job application workflow.

---

## ✨ Features

### 🤖 Automated Job Application Flow
- Loads job search results automatically
- Detects and processes **Easy Apply** jobs
- Opens Smart Apply pages
- Handles multi-tab browser flow safely

### 🧾 Smart Form Handling
- Auto-fills contact information (city & postal code)
- Handles resume selection step
- Fills relevant experience section automatically
- Supports multi-step applications

### 🧠 AI-Assisted Question Answering
Automatically detects and answers:

- Text input questions
- Textarea questions
- Dropdown selections
- Radio button selections

AI answers are generated dynamically via GPT integration (mock included for testing).

### 🧩 Robust Browser Automation
- Uses `undetected_chromedriver`
- Persistent user profile support
- Smart tab switching & cleanup
- Structured exception handling

### ⚙️ Config Driven
All configuration is handled via `.env`:

- Job limits
- Wait times
- Location data
- AI credentials

---

## 🧱 Project Structure

```

Job-Application-automate/
│
├── main.py                  # Main automation workflow
├── form_fill_action.py      # Form step handlers
├── AI_Action.py             # Question extraction & AI answering
├── gpt_main.py              # GPT integration layer
├── config.py                # Environment configuration
│
├── utils/
│   ├── driver.py            # Chrome driver initialization
│   └── print_exception.py   # Structured error logger
│
├── .env                     # Local environment variables (NOT uploaded)
├── requirements.txt
└── README.md

```

---

## ⚙️ How It Works

### 1️⃣ Driver Initialization
- Launches Chrome using `undetected_chromedriver`
- Uses a persistent local Chrome profile
- Helps reduce bot detection

---

### 2️⃣ Job Collection
The bot:

- Opens the configured job search URL
- Detects job cards
- Scrolls to load more jobs
- Filters jobs containing **Easy Apply**

---

### 3️⃣ Application Flow

```

Job Card
↓
Open Easy Apply
↓
Fill Contact Info
↓
AI Answers Questions
↓
Fill Experience Section
↓
Submit Application

````

---

### 4️⃣ AI Question Engine

The system scans question containers dynamically (`q_0 → q_100`) and detects:

| Question Type | Handling |
|---|---|
| Text Input | AI-generated answer |
| Textarea | AI-generated answer |
| Dropdown | AI selects best match |
| Radio Buttons | AI selects matching option |

---

## 🧠 AI Integration

Main AI functions:

```python
new_chatgpt_chat_withID()
new_chatgpt_chat_withID_for_drop_down()
````

Current version includes:

* Mock AI responses (safe for testing)
* Ready structure for real OpenAI prompt-based integration

---

## 🔧 Environment Variables (.env)

Create a `.env` file in the project root:

```env
gpt_API_kye=sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
gpt_Prompt_id=1234567788

JOB_SEARCH_URL=https://www.glassdoor.co.in/Job/index.htm
WAIT_BETWEEN_APPS=15
MAX_APPLICATIONS=5

POSTAL_CODE=560001
CITY=Banglore, Karnataka
JOB_TITLE=Software Engineer
COMPANY=XYZ
```

⚠️ Never upload your real API keys to GitHub.

---

## 📦 Requirements

Create `requirements.txt`:

```
selenium
undetected-chromedriver
python-dotenv
openai
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

```bash
python main.py
```

---

## 🔐 First-Time Setup Requirement

When running the bot for the first time:

1. The browser will open.
2. You must manually log in.
3. Upload your resume manually once.

### Why?

The system uses a persistent Chrome profile.
Once logged in, your session is saved locally.

From the next run onward:

* The script automatically opens your logged-in profile.
* No need to log in again (unless logged out manually).

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

GitHub:
[https://github.com/junedkhan9310/Job-Application-automate.git](https://github.com/junedkhan9310/Job-Application-automate.git)
