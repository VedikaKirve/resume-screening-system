from sklearn.feature_extraction.text import TfidfVectorizer

def get_vectors(resumes, job_desc):
    documents = resumes + [job_desc]   # 👈 VERY IMPORTANT

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(documents)

    return vectors