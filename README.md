# 📄 Resume Screening System
A Smart Resume Screening System that ranks candidates based on job description relevance using Natural Language Processing (NLP).

## 🔍 Problem
Manual resume screening is time-consuming and inefficient when handling large volumes of applications.

## 💡 Solution
Developed an NLP-based Resume Screening System using TF-IDF and cosine similarity to automatically rank candidates based on job description relevance and skill matching.

## 📌 Project Overview

This project automates the process of screening resumes by comparing them with a job description and ranking candidates based on relevance.

It uses **TF-IDF vectorization** and **cosine similarity** to measure how closely a resume matches the job requirements.

## ✨ Features

- 📄 Upload multiple resumes (PDF)
- 🧠 Extract required skills from job description
- 📊 Rank candidates based on similarity score
- 🎯 Final score combining:
- Text similarity
- Skill match percentage
- 📋 Detailed breakdown of results
- 📥 Download candidate report
- ⚡ Fast and lightweight (no heavy ML models)

## 🛠️ Tech Stack

- **Python**
- **Streamlit** (UI & deployment)
- **NLP** (TF-IDF, cosine similarity)
- **NLTK / Text preprocessing**
- **Pandas**

## ⚙️ How It Works

1. User enters a job description
2. Uploads multiple resumes (PDF)
3. Text is extracted and cleaned
4. TF-IDF vectors are created
5. Cosine similarity is calculated
6. Skills are matched
7. Final score is computed and displayed

## 🧠 Scoring Logic
Final Score = 0.5 × Text Similarity + 0.5 × Skill Match

## 📸 Screenshots
(Add images)

## 🚀 Deployment
Deployed using Streamlit Cloud

## 🧩 Challenges Faced
Handling PDF text extraction issues
Debugging NumPy vs float conversion errors
Ensuring smooth deployment on Streamlit

## 🧩 Challenges Faced
Handling PDF text extraction issues
Debugging NumPy vs float conversion errors
Ensuring smooth deployment on Streamlit

## 📦 Installation (Local Setup)
-git clone https://github.com/VedikaKirve/resume-screening-system.git
-cd resume-screening-system
-pip install -r requirements.txt
-streamlit run app/app.py

## 🌍 Live Demo
https://resume-screening-system-app.streamlit.app/

## Author
**Vedika Kirve**
This project is part of my portfolio, showcasing the NLP skills essential for data science roles. If you have any questions, feedback, or would like to collaborate, feel free to get in touch!

Email: vedikakirve6@gmail.com  
LinkedIn: www.linkedin.com/in/vedikakirve06  
GitHub: https://github.com/VedikaKirve

