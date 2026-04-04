SKILLS = ["python", "sql", "machine learning", "excel", "tableau"]

def extract_skills(text):
    found = []
    
    for skill in SKILLS:
        if skill in text:
            found.append(skill)
    
    return found

