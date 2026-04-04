import streamlit as st
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

@st.cache_resource
def load_model():
    return SentenceTransformer('all-MiniLM-L6-v2')

model = load_model()

def get_bert_similarity(resumes, job_desc):
    job_embedding = model.encode([job_desc])

    resume_embeddings = model.encode(resumes)

    scores = cosine_similarity(job_embedding, resume_embeddings)

    return scores[0]