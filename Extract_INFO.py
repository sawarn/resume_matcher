import PyPDF2
import re
import csv
import os

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

# Function to extract uppercase phrases with numbers, brackets, hyphens, and slashes
def extract_uppercase_phrases(text):
    return re.findall(r'([A-Z\s\(\),/-]+\d*[A-Z\d\s\(\),/-]*)(?![a-z])', text)

# Function to extract section information from text
def extract_section(text, section_header):
    # Define a regular expression pattern to match the section entries
    section_pattern = r"{}([\s\S]+?)(?=(?:{}|$))".format(section_header, "|".join(["Work History", "Interests", "Education", "Community Service", "Skills"]))
    
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

# Function to extract education information
def extract_education(text):
    # Extract education section
    education_section = extract_section(text, "Education")
    
    # Split the education section into individual entries based on newline
    education_list = education_section.split('\n')
    
    return education_list

# Function to extract the job role from a PDF file
def extract_job_role(pdf_path):
    extracted_text = extract_text_from_pdf(pdf_path)
    
    if extracted_text:
        # Extract job role from the first line
        job_roles = extract_uppercase_phrases(extracted_text.split('\n')[0])
        return job_roles[0] if job_roles else ""
    else:
        return ""

# Function to process PDF files in a directory
def process_pdfs_in_directory(directory_path, output_csv_file):
    with open(output_csv_file, mode="w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Department", "File Name", "Education", "Skills", "Job Role"])
        
        for department in os.listdir(directory_path):
            department_path = os.path.join(directory_path, department)
            if os.path.isdir(department_path):
                for root, _, files in os.walk(department_path):
                    for file_name in files:
                        if file_name.endswith(".pdf"):
                            pdf_path = os.path.join(root, file_name)
                            file_name_without_ext = os.path.splitext(file_name)[0]
                            extracted_text = extract_text_from_pdf(pdf_path)
                            
                            if extracted_text:
                                # Extract education information
                                education_info = extract_education(extracted_text)
                                
                                # Extract skills information
                                skills_info = extract_skills(extracted_text)
                                
                                # Extract the job role
                                job_role = extract_job_role(pdf_path)
                                
                                # Write the data to the CSV file
                                writer.writerow([department, file_name_without_ext, "\n".join(education_info), "\n".join(skills_info), job_role])

def main():
    input_directory = "/Users/sawarn/Downloads/resume_matcher/archive/data/data"
    output_csv = "/Users/sawarn/Downloads/resume_matcher/resume_info.csv"
    
    process_pdfs_in_directory(input_directory, output_csv)

if __name__ == "__main__":
    main()
