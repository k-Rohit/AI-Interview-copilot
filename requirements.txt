An intelligent interview preparation tool that generates tailored candidate summaries and technical interview questions using AI. Built with LangChain, OpenAI GPT-4, FastAPI, and Streamlit.

🚀 Features
Smart Resume Analysis - Extract and analyze resume content from PDF/TXT files
Tailored Candidate Summaries - AI-generated summaries highlighting relevant skills and experience
Technical Interview Questions - Generate 6 role-specific technical questions focusing on:
Deep technical concepts and implementations
Problem-solving scenarios
System design challenges
Debugging and optimization skills
Export Results - Download summaries and questions as TXT or JSON
Real-time Processing - Fast PDF text extraction using PyMuPDF
Professional UI - Clean, intuitive Streamlit interface
🛠 Tech Stack
Component	Technology
Backend	FastAPI + Python 3.12
AI/ML	LangChain + OpenAI GPT-4
Frontend	Streamlit
PDF Processing	PyMuPDF (fitz)
HTTP Client	Requests
Environment	python-dotenv
📋 Prerequisites
Python 3.8 or higher
OpenAI API key (GPT-4 access recommended)
4GB+ RAM for optimal performance
⚡ Quick Start
1. Clone the Repository
git clone https://github.com/yourusername/ai-interview-assistant.git
cd ai-interview-assistant
2. Install Dependencies
pip install -r requirements.txt
3. Configure Environment
Create a .env file in the project root:

OPENAI_API_KEY=sk-your-openai-api-key-here
4. Run the Application
Terminal 1 - Start Backend:

cd backend
python main.py
✅ Backend will run on http://localhost:8001

Terminal 2 - Start Frontend:

cd frontend
streamlit run app.py
✅ Frontend will open at http://localhost:8501

5. Start Interviewing!
Upload a candidate's resume (PDF or TXT)
Paste the job description
Click "Generate Summary & Questions"
Export results for your interview