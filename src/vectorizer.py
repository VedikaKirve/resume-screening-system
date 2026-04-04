from sklearn.feature_extraction.text import TfidfVectorizer

def get_vectors(resumes, job_desc):
    corpus = resumes + [job_desc]
    
    tfidf = TfidfVectorizer()
    vectors = tfidf.fit_transform(corpus)
    
    return vectors