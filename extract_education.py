import PyPDF2
import re
import csv

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_path):
    pdf_text = ""
    try:
        with open(pdf_path, "rb") as pdf_file:
            pdf_reader = PyPDF2.PdfFileReader(pdf_file)
            for page_num in range(pdf_reader.numPages):
                page = pdf_reader.getPage(page_num)
                pdf_text += page.extractText()
    except Exception as e:
        print(f"Error extracting text from PDF: {str(e)}")
    return pdf_text

# Function to extract education information from text and remove unnecessary newlines
def extract_education(text):
    # Define a regular expression pattern to match education entries
    education_pattern = r"Education\s*([\s\S]+?)(?=(?:Skills|\Z))"
    
    # Find all matches in the text
    education_matches = re.findall(education_pattern, text)
    
    # Remove unnecessary newline characters and extra whitespace
    cleaned_education = [re.sub(r'\n\s*', ' ', entry).strip() for entry in education_matches]
    
    return cleaned_education

# Function to save education data to a CSV file
def save_education_to_csv(education_info, csv_file):
    with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Education"])  # Write the header
        for entry in education_info:
            writer.writerow([entry])

# Main function
def main():
    pdf_resume_path = "/Users/sawarn/Downloads/resume_matcher/archive/data/data/BPO/45077654.pdf"
    extracted_text = extract_text_from_pdf(pdf_resume_path)
    
    if extracted_text:
        education_info = extract_education(extracted_text)
        print(education_info)
        if education_info:
            # Save education information to a CSV file
            save_education_to_csv(education_info, "education_data.csv")

if __name__ == "__main__":
    main()
