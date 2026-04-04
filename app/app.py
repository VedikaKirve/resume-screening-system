import sys
import os
import math

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st

from src.pdf_extractor import extract_text
from src.preprocessing import clean_text
from src.vectorizer import get_vectors
from src.similarity import calculate_similarity
from src.ranking import rank_candidates
from src.skills_extractor import extract_skills

st.title("📄 Resume Screening System")

job_desc = st.text_area("Enter Job Description")
files = st.file_uploader("Upload Resumes", accept_multiple_files=True)

if st.button("Analyze"):

    st.subheader("📊 Resume Ranking Results")
    st.progress(70)

    resumes = []
    names = []

    # ✅ Step 1: Process resumes FIRST
    for file in files:
        text = extract_text(file)
        clean = clean_text(text)

        resumes.append(clean)
        names.append(file.name)

    # ✅ Step 2: Clean job description
    job_clean = clean_text(job_desc)

    # ✅ Step 3: Skills extraction
    skills = extract_skills(job_clean)
    st.markdown("### 🧠 Required Skills")

    for skill in skills:
        st.write(f"✅ {skill.capitalize()}")

    # ✅ Step 4: ML processing
    vectors = get_vectors(resumes, job_clean)
    scores = calculate_similarity(vectors)

    ranked = sorted(zip(names, scores, resumes), key=lambda x: x[1], reverse=True)

    # ✅ Step 5: Show results
    st.success(f"🏆 Top Candidate: {ranked[0][0]}")

    for name, score, resume_text in ranked:
        percentage = score * 100

    # ✅ Skill match logic
    matched_skills = [skill for skill in skills if skill in resume_text]
    skill_match_percent = (len(matched_skills) / len(skills)) * 100 if skills else 0

    tfidf_percent = score * 100
    skill_percent = skill_match_percent

    final_score = (0.5 * tfidf_percent) + (0.5 * skill_percent) 

    st.write(f"📄 {name}")

    if isinstance(percentage, (int, float)) and not math.isnan(percentage):
        progress_value = int(min(max(percentage, 0), 100))
        st.progress(progress_value)
    else:
        st.progress(0)
    if isinstance(final_score, (int, float)) and not math.isnan(final_score):
        st.success(f"🎯 Final Score: {final_score:.2f}%")
    else:
        st.success("🎯 Final Score: 0.00%")

    with st.expander("📊 Detailed Breakdown"):
        st.write(f"📊 Text Similarity: {tfidf_percent:.2f}%")
        st.write(f"🧠 Skill Match: {skill_percent:.2f}%")

    # Show matched skills
    st.markdown("### ✅ Matched Skills")
    for skill in matched_skills:
        st.write(f"✅ {skill.capitalize()}")

    st.markdown("---")

    missing_skills = [skill for skill in skills if skill not in resume_text]

    st.markdown("### ❌ Missing Skills")
    for skill in missing_skills:
        st.write(f"❌ {skill.capitalize()}")

    if skill_match_percent > 70:
        st.success("💪 Strong Match")
    elif skill_match_percent > 40:
        st.warning("⚠️ Moderate Match")
    else:
        st.error("❌ Weak Match")

    if not files or not job_desc:
        st.warning("Please upload resumes and enter job description")

    st.info(f"Out of {len(skills)} required skills, {len(matched_skills)} matched")

    report = f"""
    Candidate: {name}
    Match Score: {percentage:.2f}%
    Skill Match: {skill_match_percent:.2f}%

    Matched Skills: {", ".join(matched_skills)}
    Missing Skills: {", ".join(missing_skills)}
    """

    st.download_button("📥 Download Report", report, file_name="report.txt")