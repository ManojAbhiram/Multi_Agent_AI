# 🤖 Multi-Agent AI System

A Python-based multi-agent AI system that classifies and routes PDF, JSON, and Email inputs to specialized agents using LLMs and shared memory.

---

## 🧠 Features

- **Classifier Agent**: Detects input format (PDF, JSON, Email) and intent (Invoice, RFQ, Complaint, Regulation, etc.)
- **JSON Agent**: Validates and normalizes structured JSON data, flags anomalies
- **Email Agent**: Extracts sender, intent, urgency, and formats for CRM usage
- **Shared Memory (SQLite)**: Stores source, type, timestamp, extracted fields, and conversation IDs for traceability

---

## 🛠️ Tech Stack

- Python 3.8+
- `pdfminer.six` for PDF text extraction
- `requests` for API calls (e.g., AIMLAPI/OpenAI)
- SQLite for lightweight shared memory
- AIMLAPI (GPT-4o-mini) or OpenAI for NLP tasks

---

## 📁 Folder Structure

multi_agent_ai/

├── agents/

│ ├── classifier_agent.py

│ ├── email_agent.py

│ └── json_agent.py

├── memory/

│ └── shared_memory.py

├── utils/

│ ├── file_utils.py

│ └── openai_utils.py

├── inputs/

│ ├── sample_email.txt

│ ├── sample_invoice.pdf


│ └── sample_data.json

├── main.py

├── requirements.txt

└── README.md

---

## 🚀 Getting Started

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Set your API key environment variable
```bash
# Windows CMD
set AIML_API_KEY=your_api_key_here

# macOS/Linux
export AIML_API_KEY=your_api_key_here
```

### 3. Run the system
```bash
python main.py
```
---

## 📄 Sample Inputs

inputs/sample_email.txt — example email text

inputs/sample_data.json — example JSON invoice or document

inputs/sample_invoice.pdf — example PDF invoice

---

## 🧪 Sample Output

Processing: inputs/sample_email.txt

[Classifier] Detected format: Email, intent: RFQ

[Email Agent] Extracted sender: customer@example.com, urgency: high

Shared memory updated for thread ID: email_12345





Processing: inputs/sample_data.json

[Classifier] Detected format: JSON, intent: Invoice

[JSON Agent] Normalized data, missing fields: None

Shared memory updated for thread ID: json_ABC001

---

## 🔮 Future Improvements

Add PDF Agent for advanced invoice parsing

Switch SQLite to Redis for distributed shared memory

Wrap system as a REST API for integration
