Resume Matcher
Table of Contents
About
Getting Started
Prerequisites
Installation
Usage
Fetching Job Descriptions
Matching CVs
Results
Contributing
License
Acknowledgments
About
The Resume Matcher is a Python-based project that matches job applicants' resumes (CVs) with job descriptions based on skills and education. It utilizes Hugging Face Transformers to preprocess text data and calculate similarity scores using DistilBERT embeddings.

Getting Started
Prerequisites
Before using the Resume Matcher, ensure you have the following prerequisites installed:

Python 3.x
Git
pip (Python package manager)
You can install Python from python.org, Git from git-scm.com, and pip comes bundled with Python.

Installation
Clone the project repository:

bash
Copy code
git clone https://github.com/sawarn/resume_matcher.git
Change the working directory to the project folder:

bash
Copy code
cd resume_matcher
Install the required Python packages:

bash
Copy code
pip install -r requirements.txt
Usage
The Resume Matcher workflow consists of three main steps: fetching job descriptions, matching CVs, and viewing results.

Fetching Job Descriptions
Use the Hugging Face Datasets library to fetch job descriptions. For example:

python
Copy code
python fetch_job_descriptions.py
Job descriptions will be saved in CSV format.

Matching CVs
Prepare a CSV file containing CV details in the following format:

arduino
Copy code
Department, File Name, Education, Skills, Job Role
Match CVs against job descriptions:

python
Copy code
python match_cvs.py
Results
The matching results will be saved in a CSV file, showing the top CVs for each job description based on similarity scores.

Contributing
We welcome contributions! If you'd like to contribute to this project, please follow these steps:

Fork the repository.
Create a new branch for your feature or bug fix.
Make your changes and commit them with clear messages.
Push your changes to your fork.
Create a pull request to merge your changes into the main branch.
Please make sure to follow our Code of Conduct.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Hugging Face Transformers
Python
Pandas
Scikit-learn
