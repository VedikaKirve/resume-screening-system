# 📄 Resume Screening System
An intelligent Resume Screening System that analyzes and ranks resumes based on a given job description using Natural Language Processing (NLP) and Machine Learning techniques.
🚀 Live App: https://resume-screening-system-m6rbvdhdsndztgmlynppdn.streamlit.app/


## 📌 Project Overview
This project simulates a real-world Applicant Tracking System (ATS) used by recruiters to filter and rank candidates.
Unlike traditional ATS tools, this system not only ranks resumes but also provides:

📊 Skill match insights
❌ Missing skill detection
💡 Resume improvement suggestions
🧠 Explainable results (Why this candidate?)


## 🔍 Problem
Manual resume screening is time-consuming, inconsistent, and often relies on basic keyword matching, leading to inefficient candidate selection.


## 💡 Solution
Developed an AI-based Resume Screening System using TF-IDF and cosine similarity to automatically rank candidates, provide skill gap analysis, and deliver explainable insights through an interactive dashboard.


## ✨ Features

### 🔍 Resume Analysis
Extracts text from uploaded PDF resumes
Cleans and preprocesses textual data

### 📊 Smart Ranking System
Uses TF-IDF Vectorization
Computes Cosine Similarity
Ranks candidates based on relevance to job description

### 🧠 Explainable AI (XAI)
Shows why a candidate is selected
Highlights matched and missing skills
Provides actionable suggestions

### 🎯 Role Prediction
Predicts candidate role (Data Analyst, ML Engineer, etc.)
Based on keyword logic

### 📈 Interactive Dashboard
Candidate comparison bar chart
Progress bars and scoring system
Detailed breakdown for each candidate

### 📄 Report Generation
Downloadable report for each candidate

### 🌐 Live Deployment
Fully deployed using Streamlit Cloud


## 🛠️ Tech Stack

- Frontend/UI: Streamlit
- Backend: Python
- Libraries:
-- pandas
-- numpy
-- scikit-learn
-- PyMuPDF
- ML Techniques:
-- TF-IDF Vectorization
-- Cosine Similarity


## ⚙️ How It Works

1. Upload multiple resumes (PDF format)
2. Enter a job description
3. System processes and analyzes resumes
4. Generates:
- Ranking of candidates
- Skill match percentage
- Missing skills
- Final score
5. Displays results in an interactive dashboard


## 🧠 Scoring Logic
Final Score = 0.5 × Text Similarity + 0.5 × Skill Match


## 📸 Screenshots
(Add images)


## 🚀 Deployment
Deployed using Streamlit Cloud


## 🧩 Challenges Faced
- Handling PDF text extraction issues
- Debugging NumPy vs float conversion errors
- Ensuring smooth deployment on Streamlit


## 🚀 Future Enhancements
- 🤖 AI-based resume feedback (LLM integration)
- 🧠 Semantic similarity using BERT
- 🔐 User authentication system
- 📊 Advanced analytics dashboard
- 🌍 Multi-language resume support


## 🎯 Learning Outcomes
- Applied NLP techniques in a real-world problem
- Built an end-to-end ML project
- Designed an interactive dashboard
- Deployed a production-ready web app


## 📦 Installation (Local Setup)
- git clone https://github.com/VedikaKirve/resume-screening-system.git
- cd resume-screening-system
- pip install -r requirements.txt
- streamlit run app/app.py


## 🌍 Live Demo
https://resume-screening-system-m6rbvdhdsndztgmlynppdn.streamlit.app/


## Author
**Vedika Kirve**
This project is part of my portfolio, showcasing the NLP skills essential for data science roles. If you have any questions, feedback, or would like to collaborate, feel free to get in touch!

Email: vedikakirve6@gmail.com  
LinkedIn: www.linkedin.com/in/vedikakirve06  
GitHub: https://github.com/VedikaKirve

