import streamlit as st
import requests
import re
import fitz  # PyMuPDF for PDF text extraction
from typing import Dict, Any
from config import API_BASE_URL, INTERVIEW_TYPES_FILE, TRANSCRIPT_FILE
import io
from openai import OpenAI

# Function to make API requests to the backend
def make_api_request(endpoint: str, files: Dict = None, data: Dict = None, api_key: str = None) -> Dict[str, Any]:
    """Generic API request handler."""
    try:
        url = f"{API_BASE_URL}{endpoint}"  # Construct the full API URL
        headers = {"Authorization": f"Bearer {api_key}"} if api_key else {}  # Add API key to headers if provided
        response = requests.post(url, files=files, data=data, headers=headers, timeout=60)  # Make POST request
        if response.status_code == 200:
            return response.json()  # Return JSON response if successful
        else:
            # Handle errors and extract error messages
            try:
                error_msg = response.json().get('detail', f'HTTP {response.status_code}')
            except:
                error_msg = f'HTTP {response.status_code}: {response.text}'
            raise Exception(error_msg)
    except requests.exceptions.Timeout:
        raise Exception("Request timed out.")  # Handle timeout errors
    except requests.exceptions.ConnectionError:
        raise Exception("Cannot connect to the backend server.")  # Handle connection errors
    except Exception as e:
        raise Exception(str(e))  # Handle other exceptions

# Function to extract text from uploaded files (PDF or TXT)
def extract_text_from_file(uploaded_file) -> str:
    """Extract text from PDF or TXT."""
    try:
        if uploaded_file.type == "application/pdf":
            # Extract text from PDF using PyMuPDF
            pdf_bytes = uploaded_file.getvalue()
            doc = fitz.open(stream=pdf_bytes, filetype="pdf")
            return "".join(page.get_text() for page in doc)  # Concatenate text from all pages
        elif uploaded_file.type in ["text/plain", "application/octet-stream"]:
            # Extract text from plain text files
            return uploaded_file.getvalue().decode("utf-8")
        return ""
    except Exception:
        return ""  # Return empty string if extraction fails

# Function to load interview types from a file
def load_interview_types(file_path=INTERVIEW_TYPES_FILE):
    """Read interview types from a file."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]  # Read and return non-empty lines
    except FileNotFoundError:
        st.error(f"Interview type file not found: {file_path}")  # Display error if file is missing
        return []

# Function to display AI-generated questions in a structured format
def display_structured_questions(raw_text: str):
    """Display AI-generated questions without headings."""
    lines = raw_text.strip().split('\n')  # Split text into lines
    for q in lines:
        q = re.sub(r'^\d+\.\s*', '', q.strip())  # Remove numbering if present
        if q:
            st.markdown(f"- {q}")  # Display each question as a bullet point

# Function to show a progress bar with a message
def show_progress(message, progress):
    """Helper to show progress bar."""
    status_text = st.empty()  # Create an empty placeholder for the status text
    status_text.text(message)  # Display the message
    progress_bar = st.progress(progress)  # Display the progress bar
    return status_text, progress_bar

# Function to use text-to-speech (TTS) to speak text
def speak_tts(client, text):
    """Speak text using GPT-4o-mini-TTS directly in memory."""
    audio_buffer = io.BytesIO()  # Create an in-memory buffer for audio
    with client.audio.speech.with_streaming_response.create(
        model="gpt-4o-mini-tts",  # Specify the TTS model
        voice="coral",  # Specify the voice
        input=text,  # Input text to be spoken
        instructions="Speak in a professional and clear tone."  # Instructions for the voice
    ) as response:
        for chunk in response.iter_bytes():
            audio_buffer.write(chunk)  # Write audio chunks to the buffer

    audio_buffer.seek(0)  # Reset the buffer pointer to the beginning
    st.audio(audio_buffer, format="audio/mp3")  # Play the audio in Streamlit

# Function to transcribe audio to text using OpenAI's Whisper model
def transcribe_audio(client, audio_file):
    """Transcribe recorded audio to text."""
    transcription = client.audio.transcriptions.create(
        model="whisper-1",  # Specify the transcription model
        file=audio_file  # Input audio file
    )
    return transcription.text  # Return the transcribed text

# Function to save a question and answer pair to a transcript file
def save_transcript_to_file(question, answer):
    """Append question and answer to a text file."""
    with open(TRANSCRIPT_FILE, "a", encoding="utf-8") as f:
        f.write(f"Q: {question}\n")  # Write the question
        f.write(f"A: {answer}\n\n")  # Write the answer

# Function to clear the transcript file
def clear_transcript_file():
    """Clear the transcript file."""
    with open(TRANSCRIPT_FILE, "w", encoding="utf-8") as f:
        f.write("")  # Overwrite the file with an empty string