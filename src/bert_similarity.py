from sentence_transformers import SentenceTransformer, util

# Load model once
model = SentenceTransformer('all-MiniLM-L6-v2')

def get_bert_similarity(resumes, job_desc):
    scores = []

    job_embedding = model.encode(job_desc)

    for resume in resumes:
        resume_embedding = model.encode(resume)
        similarity = util.cos_sim(resume_embedding, job_embedding)
        scores.append(similarity.item())

    return scores