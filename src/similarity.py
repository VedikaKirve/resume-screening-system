from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(vectors):
    job_vector = vectors[-1]
    resume_vectors = vectors[:-1]

    scores = cosine_similarity(resume_vectors, job_vector)

    return scores.flatten()