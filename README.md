# 🧠 AI Interview Assistant

An intelligent interview preparation tool that generates tailored candidate summaries and technical interview questions using AI. Built with LangChain, OpenAI GPT-4, FastAPI, and Streamlit.

## 🚀 Features

- **Smart Resume Analysis** - Extract and analyze resume content from PDF/TXT files
- **Tailored Candidate Summaries** - AI-generated summaries highlighting relevant skills and experience
- **Technical Interview Questions** - Generate 6 role-specific technical questions focusing on:
  - Deep technical concepts and implementations
  - Problem-solving scenarios
  - System design challenges
  - Debugging and optimization skills
- **Export Results** - Download summaries and questions as TXT or JSON
- **Real-time Processing** - Fast PDF text extraction using PyMuPDF
- **Professional UI** - Clean, intuitive Streamlit interface

## 🛠 Tech Stack

| Component | Technology |
|-----------|------------|
| **Backend** | FastAPI + Python 3.12 |
| **AI/ML** | LangChain + OpenAI GPT-4 |
| **Frontend** | Streamlit |
| **PDF Processing** | PyMuPDF (fitz) |
| **HTTP Client** | Requests |
| **Environment** | python-dotenv |

## 📋 Prerequisites

- Python 3.8 or higher
- OpenAI API key (GPT-4 access recommended)
- 4GB+ RAM for optimal performance

## ⚡ Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/ai-interview-assistant.git
cd ai-interview-assistant
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Environment
Create a `.env` file in the project root:
```bash
OPENAI_API_KEY=sk-your-openai-api-key-here
```

### 4. Run the Application

**Terminal 1 - Start Backend:**
```bash
cd backend
python main.py
```
✅ Backend will run on `http://localhost:8001`

**Terminal 2 - Start Frontend:**
```bash
cd frontend
streamlit run app.py
```
✅ Frontend will open at `http://localhost:8501`

### 5. Start Interviewing!
1. Upload a candidate's resume (PDF or TXT)
2. Paste the job description
3. Click "Generate Summary & Questions"
4. Export results for your interview

## 📁 Project Structure

```
ai-interview-assistant/
├── backend/
│   ├── main.py                 # FastAPI server
│   ├── models.py              # Pydantic data models
│   ├── chains/
│   │   ├── __init__.py
│   │   ├── summary_chain.py   # Resume summary generation
│   │   └── question_chain.py  # Interview question generation
│   └── utils/
│       └── __init__.py
├── frontend/
│   └── app.py                 # Streamlit interface
├── data/                      # Sample files (optional)
├── .env                       # Environment variables
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## 🔧 Configuration

### Environment Variables
| Variable | Description | Required |
|----------|-------------|----------|
| `OPENAI_API_KEY` | Your OpenAI API key | Yes |

### Model Configuration
You can modify the AI models in the chain files:

**For GPT-4 (Recommended):**
```python
llm = ChatOpenAI(model="gpt-4.1-nano", temperature=0.2)
```

## 📊 API Endpoints

### Backend API (`http://localhost:8000`)

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Health check |
| `/health` | GET | Extended health check with API key validation |
| `/generate-brief` | POST | Generate interview brief from resume + job description |

### Example API Usage
```python
import requests

files = {"resume": open("resume.pdf", "rb")}
data = {"job_description": "Software Engineer position..."}

response = requests.post(
    "http://localhost:8001/generate-brief",
    files=files,
    data=data
)

result = response.json()
print(result["summary"])
print(result["questions"])
```

## 🔍 Troubleshooting

### Common Issues

**1. OpenAI API Key Error**
```
Error: The api_key client option must be set
```
**Solution:** Check your `.env` file format (no quotes around the key)

**2. File Upload Error**
```
Error: Could not extract text from resume
```
**Solution:** Ensure the PDF is text-based (not scanned images)

**3. Import Error**
```
ImportError: No module named 'fitz'
```
**Solution:** Install PyMuPDF: `pip install PyMuPDF`

**4. Connection Error**
```
Cannot connect to backend server
```
**Solution:** Make sure backend is running on port 8000

---

<div align="center">

**Made with ❤️ for better hiring decisions**

[⭐ Star this repo](https://github.com/yourusername/ai-interview-assistant) | [🐛 Report Bug](https://github.com/yourusername/ai-interview-assistant/issues) | [💡 Request Feature](https://github.com/yourusername/ai-interview-assistant/issues)

</div>
