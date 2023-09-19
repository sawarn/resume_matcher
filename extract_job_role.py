import PyPDF2

# Function to extract the first line of text from a PDF file
def extract_first_line_from_pdf(pdf_path):
    try:
        with open(pdf_path, "rb") as pdf_file:
            pdf_reader = PyPDF2.PdfFileReader(pdf_file)
            if pdf_reader.numPages > 0:
                first_page = pdf_reader.getPage(0)
                first_line = first_page.extractText().split('\n')[0]  # Extract the first line
                return first_line
            else:
                return ""
    except Exception as e:
        print(f"Error extracting text: {str(e)}")
        return ""

# Main function
def main():
    pdf_resume_path = "/Users/sawarn/Downloads/resume_matcher/archive/data/data/BUSINESS-DEVELOPMENT/10501991.pdf"
    extracted_text = extract_first_line_from_pdf(pdf_resume_path)
    
    if extracted_text:
        print("Extracted First Line:")
        print(extracted_text)

if __name__ == "__main__":
    main()
