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

# Function to extract section information from text
def extract_section(text, section_header):
    # Define a regular expression pattern to match the section entries
    section_pattern = r"{}([\s\S]+?)(?=(?:{}|$))".format(section_header, "|".join(["Work History", "Interests", "Education"]))
    
    # Find the first match in the text (case-sensitive)
    section_match = re.search(section_pattern, text)
    
    # Extract the section if a match is found
    if section_match:
        section_data = section_match.group(1).strip()
        return section_data
    else:
        return ""

# Function to extract skills information
def extract_skills(text):
    # Extract skills section
    skills_section = extract_section(text, "Skills")
    
    # Split the skills section into individual skills based on newline or comma
    skills_list = re.split(r'\n|, ', skills_section)
    
    return skills_list

# Function to save section data to a CSV file
def save_section_to_csv(section_info, csv_file):
    with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([section_info])

# Main function
def main():
    pdf_resume_path = "/Users/sawarn/Downloads/resume_matcher/archive/data/data/DIGITAL-MEDIA/14761906.pdf"
    extracted_text = extract_text_from_pdf(pdf_resume_path)
    
    if extracted_text:
        # Extract skills information
        skills_info = extract_skills(extracted_text)
        print(skills_info)
        if skills_info:
            # Save skills information to a CSV file
            save_section_to_csv(skills_info, "skills_data.csv")

if __name__ == "__main__":
    main()
