import speech_recognition as sr
import nltk
import spacy
import re
import os
os.environ["USE_TF"] = "0"  # Disable TensorFlow
from transformers import pipeline
from docx import Document

# Load resources
nltk.download('punkt')
nlp = spacy.load("en_core_web_sm")
summarizer = pipeline("summarization")
generator = pipeline("text-generation", model="gpt2")

# Step 1: Record voice and convert to text
def record_audio():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    print("🎤 Speak your idea (10 sec limit)...")
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, phrase_time_limit=10)
    try:
        text = recognizer.recognize_google(audio)
        print("✅ Transcription:", text)
        return text
    except sr.UnknownValueError:
        print("❌ Could not understand audio.")
        return ""
    except sr.RequestError as e:
        print(f"API Error: {e}")
        return ""

# Step 2: Clean and preprocess text
def clean_text(raw_text):
    raw_text = re.sub(r'\s+', ' ', raw_text)  # Remove extra spaces
    raw_text = raw_text.strip()
    return raw_text

# Step 3: Generate structured content
def generate_format(text, mode='blog'):
    if mode == 'summary':
        return summarizer(text, max_length=60, min_length=20, do_sample=False)[0]['summary_text']
    elif mode == 'email':
        prompt = f"Write a professional email based on this idea: {text}"
        return generator(prompt, max_length=150, num_return_sequences=1)[0]['generated_text']
    elif mode == 'blog':
        prompt = f"Write a short blog post on the following idea: {text}"
        return generator(prompt, max_length=200, num_return_sequences=1)[0]['generated_text']
    else:
        return text

# Step 4: Save to .docx
def save_to_doc(text, filename="output.docx"):
    doc = Document()
    doc.add_paragraph(text)
    doc.save(filename)
    print(f"📄 Document saved as {filename}")

# Main flow
if __name__ == "__main__":
    spoken_text = record_audio()
    if spoken_text:
        cleaned = clean_text(spoken_text)
        print("\nChoose Output Format: blog / summary / email")
        choice = input("Enter: ").strip().lower()
        structured = generate_format(cleaned, choice)
        print("\n📝 Generated Output:\n", structured)
        save_to_doc(structured)
