import pandas as pd
import torch
from transformers import DistilBertTokenizer, DistilBertModel
from sklearn.metrics.pairwise import cosine_similarity

# Load the CSV data for CVs and job descriptions
cv_data = pd.read_csv('resume_info.csv')
job_description_data = pd.read_csv('/Users/sawarn/Downloads/resume_matcher/job_description.csv')

# Load the DistilBERT tokenizer and model
tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
model = DistilBertModel.from_pretrained('distilbert-base-uncased')

# Initialize a dictionary to store the matching results
matches = {}

# Tokenize and convert text to embeddings for CVs
cv_embeddings = []

for index, row in cv_data.iterrows():
    cv_text = str(row['Education']) + ' ' + str(row['Skills'])
    inputs = tokenizer(cv_text, return_tensors="pt", padding=True, truncation=True)
    with torch.no_grad():
        outputs = model(**inputs)
    cv_embedding = outputs.last_hidden_state.mean(dim=1).squeeze().numpy()
    cv_embeddings.append(cv_embedding)

# Tokenize and convert text to embeddings for job descriptions
job_description_embeddings = []

for index, row in job_description_data.iterrows():
    job_description = row['Job Description']
    inputs = tokenizer(job_description, return_tensors="pt", padding=True, truncation=True)
    with torch.no_grad():
        outputs = model(**inputs)
    job_description_embedding = outputs.last_hidden_state.mean(dim=1).squeeze().numpy()
    job_description_embeddings.append(job_description_embedding)

# Match CVs to job descriptions based on cosine similarity
for i, job_description_embedding in enumerate(job_description_embeddings):
    job_description = job_description_data.loc[i, 'Job Description']
    similarities = cosine_similarity([job_description_embedding], cv_embeddings)
    top_matches = [(cv_data.loc[j, 'File Name'], similarities[0][j]) for j in similarities.argsort()[0][::-1][:5]]
    matches[job_description] = top_matches

# Save the matching results to a new CSV or data structure
matching_results = pd.DataFrame.from_dict(matches, orient='index', columns=['Top CV', 'Similarity Score'])
matching_results.index.name = 'Job Description'
matching_results.to_csv('matching_results.csv')
