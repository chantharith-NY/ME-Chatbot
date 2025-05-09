import PyPDF2

def extract_text_from_pdf(pdf_path):
    """
    Extract text from a PDF file
    """
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text

def preprocess_pdf(pdf_path):
    """
    Extract and preprocess the content from the PDF
    """
    raw_text = extract_text_from_pdf(pdf_path)
    # You can add more text preprocessing steps here (e.g., cleaning, splitting, etc.)
    return raw_text

if __name__ == "__main__":
    # Example usage
    pdf_text = preprocess_pdf("/Users/nychanthrith/Documents/Chantharith/ME-Chatbot/ai-model/data/raw_pdfs/Institute of Technology of Cambodia.pdf")
    with open("/Users/nychanthrith/Documents/Chantharith/ME-Chatbot/ai-model/data/processed/preprocess_text.txt", "w") as f:
        f.write(pdf_text)
    print("Preprocessing completed.")
