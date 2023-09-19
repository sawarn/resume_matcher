import PyPDF2
import re

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_path):
    pdf_text = ""
    with open(pdf_path, "rb") as pdf_file:
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            pdf_text += page.extractText()
    return pdf_text

# Function to extract skills from text
def extract_skills_from_text(text):
    # Define a regular expression pattern to match skills
    skills_pattern = r"Skills\s*([\s\S]*?)(?:\n\n|\n\n\n|\n\n\n\n|$)"

    # Find all matches in the text
    skills_matches = re.findall(skills_pattern, text, re.DOTALL)

    # Split the matches into a list of skills
    skills_list = [skill.strip() for skill in skills_matches[0].split('\n')]

    return skills_list

# Main function
def main():
    pdf_resume_path = "/Users/sawarn/Downloads/resume_matcher/archive/data/data/BUSINESS-DEVELOPMENT/10501991.pdf"
    extracted_text = extract_text_from_pdf(pdf_resume_path)
    skills_info = extract_skills_from_text(extracted_text)

    if skills_info:
        print("Extracted Skills:")
        for skill in skills_info:
            print(skill)

if __name__ == "__main__":
    main()

