def rank_candidates(scores, filenames):
    results = list(zip(filenames, scores))
    
    return sorted(results, key=lambda x: x[1], reverse=True)