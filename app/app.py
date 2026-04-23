import sys
import os
import streamlit as st
import pandas as pd
import re

# Fix import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Imports
from src.pdf_extractor import extract_text
from src.preprocessing import clean_text
from src.vectorizer import get_vectors
from src.similarity import calculate_similarity
from src.skills_extractor import extract_skills


# ================= UI =================
st.title("📄 Resume Screening System")

job_desc = st.text_area("Enter Job Description")
files = st.file_uploader("Upload Resumes", accept_multiple_files=True)


# ================= MAIN =================
if st.button("Analyze"):

    if not files or not job_desc:
        st.warning("Please upload resumes and enter job description")

    else:
        st.subheader("📊 Resume Ranking Results")
        st.progress(30)

        resumes = []
        names = []

        # STEP 1: Process resumes
        for file in files:
            text = extract_text(file)
            clean = clean_text(text)
            resumes.append(clean)
            names.append(file.name)

        # STEP 2: Clean JD
        job_clean = clean_text(job_desc)

        # STEP 3: Extract skills
        skills = extract_skills(job_clean)

        st.markdown("### 🧠 Required Skills")
        for skill in skills:
            st.write(f"✅ {skill.capitalize()}")

        # STEP 4: Similarity
        vectors = get_vectors(resumes, job_clean)
        scores = calculate_similarity(vectors)

        # Ranking
        ranked = sorted(zip(names, scores, resumes), key=lambda x: x[1], reverse=True)

        # ================= CHART =================
        df = pd.DataFrame({
            "Candidate": names,
            "Score": [float(s) * 100 for s in scores]
        })

        st.markdown("## 📊 Candidate Comparison")
        st.bar_chart(df.set_index("Candidate"))

        # ================= TOP CANDIDATE =================
        st.markdown("## 🏆 Top Candidate")
        st.success(f"{ranked[0][0]} ({round(ranked[0][1]*100,2)}%)")

        # ================= LOOP =================
        for name, score, resume_text in ranked:

            # ---------- SCORE ----------
            try:
                if hasattr(score, "__len__"):
                    score = score[0]
                percentage = float(score) * 100
            except:
                percentage = 0

            # ---------- SKILL MATCH ----------
            matched_skills = [s for s in skills if s in resume_text]
            missing_skills = [s for s in skills if s not in resume_text]

            skill_match_percent = (len(matched_skills) / len(skills)) * 100 if skills else 0

            final_score = (0.5 * percentage) + (0.5 * skill_match_percent)

            # ---------- ROLE FIT ----------
            if "machine learning" in resume_text:
                role = "ML Engineer"
            elif "sql" in resume_text:
                role = "Data Analyst"
            elif "excel" in resume_text:
                role = "Business Analyst"
            else:
                role = "General Role"

            # ---------- EXPERIENCE ----------
            exp_match = re.findall(r"(\d+\+?\s*(?:years|yrs))", resume_text.lower())
            experience = exp_match[0] if exp_match else "Not Mentioned"

            # ================= UI CARD =================
            with st.container():
                st.divider()

                st.subheader(f"📄 {name}")
                st.write(f"📅 Experience: {experience}")
                st.write(f"🎯 Role Fit: {role}")

                # SCORE UI
                col1, col2 = st.columns([4, 1])

                with col1:
                    st.progress(int(min(max(percentage, 0), 100)))

                with col2:
                    st.metric("Score", f"{round(final_score, 2)}%")

                # ---------- BREAKDOWN ----------
                with st.expander("📊 Detailed Breakdown"):
                    st.write(f"Text Similarity: {percentage:.2f}%")
                    st.write(f"Skill Match: {skill_match_percent:.2f}%")

                # ---------- SKILLS ----------
                col1, col2 = st.columns(2)

                with col1:
                    st.markdown("### ✅ Matched Skills")
                    for s in matched_skills:
                        st.write(f"✔ {s.upper()}")

                with col2:
                    if missing_skills:
                        st.markdown("### ❌ Missing Skills")
                        for s in missing_skills:
                            st.write(f"✖ {s}")
                    else:
                        st.success("🎉 No missing skills!")

                # ---------- MATCH STRENGTH ----------
                if skill_match_percent > 70:
                    st.success("💪 Strong Match")
                elif skill_match_percent > 40:
                    st.warning("⚠️ Moderate Match")
                else:
                    st.error("❌ Weak Match")

                # ---------- WHY THIS CANDIDATE ----------
                st.markdown("### 🧠 Why this candidate?")
                reasons = []

                for s in matched_skills:
                    reasons.append(f"✔ Has {s}")

                for s in missing_skills[:2]:
                    reasons.append(f"❌ Missing {s}")

                for r in reasons[:4]:
                    st.write(r)

                # ---------- INFO ----------
                st.info(f"{len(matched_skills)}/{len(skills)} skills matched")

                # ---------- REPORT ----------
                report = f"""
Candidate: {name}
Final Score: {final_score:.2f}%
Text Similarity: {percentage:.2f}%
Skill Match: {skill_match_percent:.2f}%

Matched Skills: {", ".join(matched_skills)}
Missing Skills: {", ".join(missing_skills)}
"""

                st.download_button(
                    "📥 Download Report",
                    report,
                    file_name=f"{name}_report.txt",
                    key=f"download_{name}"
                )