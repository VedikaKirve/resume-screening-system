import sys
import os
import math
import streamlit as st

# Fix import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Imports
from src.pdf_extractor import extract_text
from src.preprocessing import clean_text
from src.vectorizer import get_vectors
from src.similarity import calculate_similarity
from src.skills_extractor import extract_skills

# UI
st.title("📄 Resume Screening System")

job_desc = st.text_area("Enter Job Description")
files = st.file_uploader("Upload Resumes", accept_multiple_files=True)

if st.button("Analyze"):

    if not files or not job_desc:
        st.warning("Please upload resumes and enter job description")
    else:
        st.subheader("📊 Resume Ranking Results")
        st.progress(30)

        resumes = []
        names = []

        # Step 1: Process resumes
        for file in files:
            text = extract_text(file)
            clean = clean_text(text)
            resumes.append(clean)
            names.append(file.name)

        # Step 2: Clean job description
        job_clean = clean_text(job_desc)

        # Step 3: Extract skills
        skills = extract_skills(job_clean)

        st.markdown("### 🧠 Required Skills")
        for skill in skills:
            st.write(f"✅ {skill.capitalize()}")

        # Step 4: TF-IDF + Similarity
        vectors = get_vectors(resumes, job_clean)
        scores = calculate_similarity(vectors)

        # DEBUG (remove later if needed)
        st.write("DEBUG SCORES:", scores)

        # Ranking
        ranked = sorted(zip(names, scores, resumes), key=lambda x: x[1], reverse=True)

        # Top candidate
        st.success(f"🏆 Top Candidate: {ranked[0][0]}")

        # Loop through candidates
        for name, score, resume_text in ranked:

            try:
                # handle numpy array properly
                if hasattr(score, "__len__"):
                    score = score[0]

                percentage = float(score) * 100
            except:
                percentage = 0

            # Skill match
            matched_skills = [skill for skill in skills if skill in resume_text]
            skill_match_percent = (len(matched_skills) / len(skills)) * 100 if skills else 0

            # Final score
            final_score = (0.5 * percentage) + (0.5 * skill_match_percent)

            # Display
            st.write(f"📄 {name}")
            st.write("CHECK %:", percentage)

            # Progress bar (safe)
            st.progress(int(min(max(percentage, 0), 100)))

            # Final score (safe)
            try:
                if not math.isnan(final_score):
                    st.success(f"🎯 Final Score: {final_score:.2f}%")
                else:
                    st.success("🎯 Final Score: 0.00%")
            except:
                st.success("🎯 Final Score: 0.00%")

            # Breakdown
            
            with st.expander("📊 Detailed Breakdown"):
                st.write(f"📊 Text Similarity: {percentage:.2f}%")
                st.write(f"🧠 Skill Match: {skill_match_percent:.2f}%")

            # Matched skills
            st.markdown("### ✅ Matched Skills")
            for skill in matched_skills:
                st.write(f"✅ {skill.capitalize()}")

            st.markdown("---")

            # Missing skills
            missing_skills = [skill for skill in skills if skill not in resume_text]

            st.markdown("### ❌ Missing Skills")
            for skill in missing_skills:
                st.write(f"❌ {skill.capitalize()}")

            # Match strength
            if skill_match_percent > 70:
                st.success("💪 Strong Match")
            elif skill_match_percent > 40:
                st.warning("⚠️ Moderate Match")
            else:
                st.error("❌ Weak Match")

            st.info(f"Out of {len(skills)} required skills, {len(matched_skills)} matched")

            # Report
            report = f"""
Candidate: {name}
Final Score: {final_score:.2f}%
Text Similarity: {percentage:.2f}%
Skill Match: {skill_match_percent:.2f}%

Matched Skills: {", ".join(matched_skills)}
Missing Skills: {", ".join(missing_skills)}
"""
            st.download_button("📥 Download Report", report, file_name="report.txt")