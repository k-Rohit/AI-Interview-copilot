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
| **Backend** | FastAPI + Python 3.12.11 |
| **AI/ML** | LangChain + OpenAI GPT-4 |
| **Frontend** | Streamlit |
| **PDF Processing** | PyMuPDF (fitz) |
| **HTTP Client** | Requests |
| **Environment** | python-dotenv |

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


### 3. Run the Application

**Terminal 1 - Start Backend:**
```bash
cd backend
python main.py
```
✅ Backend will run on `http://localhost:8000`

**Terminal 2 - Start Frontend:**
```bash
cd frontend
streamlit run app.py
```
✅ Frontend will open at `http://localhost:8501`

### 4. Start Interviewing!
1. Upload a candidate's resume (PDF or TXT)
2. Paste the job description
3. Click "Generate Summary for generating a full fledged summary of the candidate with details"
4. Click "Generate Questions for generating questions for the candidate"


## 🔍 Troubleshooting

### Common Issues

**1. OpenAI API Key Error**
```
Error: OPENAI_API_KEY not found or is invalid
```
**Solution:** Check that you have pasted the key in streamlit and its correct

**2. File Upload Error**
```
Error: Could not extract text from resume
```
**Solution:** Ensure the PDF is text-based (not scanned images)

**4. Connection Error**
```
Cannot connect to backend server
```
**Solution:** Make sure backend is running on port 8000

<div align="center">

**Made with ❤️ for better hiring decisions**

</div>
