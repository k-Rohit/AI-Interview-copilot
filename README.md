# 🧠 AI Interview Assistant

An intelligent interview preparation tool that generates tailored candidate summaries and technical interview questions using AI. Built with **LangChain**, **OpenAI GPT-4**, **FastAPI**, and **Streamlit**.

---

## 🚀 Features

### ✅ **Smart Resume Analysis**
- Extract and analyze resume content from PDF/TXT files.

### ✅ **Tailored Candidate Summaries**
- AI-generated summaries highlighting relevant skills, experience, and alignment with job descriptions.

### ✅ **Technical Interview Questions**
- Generate role-specific technical questions focusing on:
  - Deep technical concepts and implementations.
  - Problem-solving scenarios.
  - System design challenges.
  - Debugging and optimization skills.

### ✅ **Export Results**
- Download summaries and questions as TXT or JSON.

### ✅ **Real-time Processing**
- Fast PDF text extraction using **PyMuPDF**.

### ✅ **Professional UI**
- Clean, intuitive **Streamlit** interface for seamless interaction.

---

## 🌐 Live Demo

- **Frontend**: [AI Interview Assistant Frontend](https://ai-int-copilot.streamlit.app/)
- **Backend**: [AI Interview Assistant Backend](https://ai-interview-copilot-backend.onrender.com/)
- Ensure the backend URL is correct and the server is running. You may have to start the backend server by going to the backend url as currently its using free servive so it spins down after few minutes of inactivity.



---

## 🛠 Tech Stack

| Component         | Technology               |
|-------------------|--------------------------|
| **Backend**       | FastAPI + Python 3.12    |
| **AI/ML**         | LangChain + OpenAI GPT-4 |
| **Frontend**      | Streamlit                |
| **PDF Processing**| PyMuPDF (fitz)           |
| **HTTP Client**   | Requests                 |
| **Environment**   | python-dotenv            |

---

## ⚡ Quick Start (Local Development)

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/ai-interview-assistant.git
cd ai-interview-assistant
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables
Create a `.env` file in the root directory and add your OpenAI API key:
```
OPENAI_API_KEY=your_openai_api_key
```

### 4. Run the Application

#### **Terminal 1 - Start Backend:**
```bash
cd backend
python main.py
```
✅ Backend will run on `http://localhost:8000`

#### **Terminal 2 - Start Frontend:**
```bash
cd frontend
streamlit run app.py
```
✅ Frontend will open at `http://localhost:8501`

---

## 🖥️ Application Workflow

### 1. **Generate Summary**
- Upload a candidate's resume (PDF or TXT).
- Paste the job description.
- Click **"Generate Summary"** to get:
  - A detailed candidate summary.
  - Skills gap analysis.

### 2. **Generate Questions**
- Select the **interview type** (e.g., Technical, HR/Behavioral, etc.).
- Click **"Generate Questions"** to get tailored interview questions.

### 3. **AI-Powered Voice Interview**
- Conduct a voice interview using AI.
- Record answers and save transcripts for review.

---

## 📂 Project Structure

```
AI-Interview-copilot/
├── backend/
│   ├── chains/
│   │   ├── question_generator.py  # Generates interview questions
│   │   ├── summary_generator.py   # Generates candidate summaries
│   │   └── __init__.py
│   ├── models.py                  # Pydantic models for API responses
│   ├── main.py                    # FastAPI backend
│   └── __init__.py
├── frontend/
│   ├── app.py                     # Streamlit frontend
│   ├── config.py                  # Configuration for frontend
│   ├── utils.py                   # Utility functions for frontend
│   ├── interview_types.txt        # List of interview types
│   ├── interview_transcript.txt   # Stores interview transcripts
│   └── __init__.py
├── requirements.txt               # Python dependencies
├── README.md                      # Project documentation
├── .env                           # Environment variables
└── .gitignore                     # Git ignore file
```

---

## 🛠 Configuration

### Environment Variables for running locally - 
Add the following to your `.env` file:
```
OPENAI_API_KEY=your_openai_api_key
```

### Configuration File
The `frontend/config.py` file contains:
```python
API_BASE_URL = "https://ai-interview-copilot-backend.onrender.com/"  # Deployed backend URL
INTERVIEW_TYPES_FILE = "interview_types.txt"  # File for interview types
TRANSCRIPT_FILE = "interview_transcript.txt"  # File for saving transcripts
RESUME_TYPES = ["pdf", "txt"]  # Supported resume file types
```

---

## 🔍 Troubleshooting

### Common Issues

#### **1. OpenAI API Key Error**
```
Error: OPENAI_API_KEY not found or is invalid
```
**Solution:** Ensure the api key is valid

#### **2. Connection Error**
```
Cannot connect to backend server
```
**Solution:** Ensure the backend URL is correct and the server is running. You may have to start the backend server by going to the backend url as currently its using free servive so it spins down after few minutes of inactivity.

#### **4. Missing Interview Types**
```
Error: Interview type file not found
```
**Solution:** Ensure `interview_types.txt` exists in the `frontend` directory.

---

---

<div align="center">
Made with ❤️ for better hiring decisions.
</div>
