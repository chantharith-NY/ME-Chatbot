import pdfplumber
import os
import re

DATA_DIR = "/Users/nychanthrith/Documents/Chantharith/ME-Chatbot/ai-model/data/raw_pdfs"
OUTPUT_FILE = "/Users/nychanthrith/Documents/Chantharith/ME-Chatbot/ai-model/data/processed/preprocess_text.txt"

def extract_text_from_pdfs(data_dir):
    text_data = []
    for file in os.listdir(data_dir):
        if file.endswith(".pdf"):
            pdf_path = os.path.join(data_dir, file)
            with pdfplumber.open(pdf_path) as pdf:
                for page in pdf.pages:
                    text = page.extract_text()
                    if text:
                        text_data.append(clean_text(text))
    return "\n".join(text_data)

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
    text = re.sub(r'[^a-zA-Z0-9.,!? ]', '', text)  # Keep only relevant characters
    return text.strip()

if __name__ == "__main__":
    extracted_text = extract_text_from_pdfs(DATA_DIR)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(extracted_text)
    print(f"Extracted text saved to {OUTPUT_FILE}")
