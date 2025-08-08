from fastapi import FastAPI, UploadFile, Form, HTTPException
from typing import Dict, Any
from fastapi.middleware.cors import CORSMiddleware
import logging
import os
from models import SummaryResponse, QuestionsResponse # your Pydantic model for response
import fitz  # PyMuPDF

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from chains.question_generator import generate_questions_chain
from chains.summary_generator import generate_summary_chain

app = FastAPI(
    title="AI Interview Assistant",
    description="Generate candidate summaries and interview questions using AI",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8501"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

def extract_text_with_pymupdf(file, filename: str) -> str:
    try:
        file.seek(0)
        if filename.lower().endswith('.pdf'):
            pdf_bytes = file.read()
            pdf_document = fitz.open(stream=pdf_bytes, filetype="pdf")
            text_content = [pdf_document[page_num].get_text() for page_num in range(pdf_document.page_count)]
            pdf_document.close()
            return "\n".join(text_content)
        elif filename.lower().endswith('.txt'):
            content = file.read()
            if isinstance(content, bytes):
                return content.decode('utf-8')
            return str(content)
        else:
            raise Exception(f"Unsupported file type: {filename}")
    except Exception as e:
        logger.error(f"PyMuPDF extraction failed: {str(e)}")
        raise Exception(f"Failed to process file: {str(e)}")

@app.post("/generate-summary", response_model=SummaryResponse)
async def generate_summary(
    resume: UploadFile,
    job_description: str = Form(...)
) -> Dict[str, Any]:
    if not resume or not job_description.strip():
        raise HTTPException(status_code=400, detail="Resume and job description are required")

    filename = resume.filename.lower() if resume.filename else ""
    if not any(filename.endswith(ext) for ext in ['.pdf', '.txt']):
        raise HTTPException(status_code=400, detail="Unsupported file type. Upload PDF or TXT only.")

    resume_text = extract_text_with_pymupdf(resume.file, resume.filename)
    if not resume_text.strip():
        raise HTTPException(status_code=400, detail="Could not extract text from resume.")

    summary_chain = generate_summary_chain()
    summary = summary_chain.run({
        "resume": resume_text,
        "job_description": job_description
    })

    return {
        "summary": summary.strip()
    }

@app.post("/generate-questions",response_model=QuestionsResponse)
async def generate_questions(
    resume_text: str = Form(...),
    job_description: str = Form(...),
    interview_type: str = Form(...)
):
    if not resume_text.strip() or not job_description.strip() or not interview_type.strip():
        raise HTTPException(status_code=400, detail="All fields are required")

    question_chain = generate_questions_chain()
    questions_raw = question_chain.run({
        "resume": resume_text,
        "job_description": job_description,
        "interview_type": interview_type
    })

    questions = []
    for line in questions_raw.split('\n'):
        line = line.strip()
        if line and len(line) > 10:
            if line[0].isdigit() and '.' in line[:5]:
                line = line.split('.', 1)[1].strip()
            questions.append(line)

    if not questions:
        questions = ["Could you walk me through your relevant experience for this role?"]

    return {
        "questions": questions
    }

@app.get("/health")
async def health_check():
    """Extended health check with API key validation"""
    try:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            return {"status": "error", "message": "OpenAI API key not configured"}
        
        return {
            "status": "healthy",
            "message": "All systems operational",
            "openai_configured": bool(api_key)
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001,reload=True)
