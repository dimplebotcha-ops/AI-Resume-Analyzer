import streamlit as st

st.title("AI Resume & Job Description Analyzer")

resume = st.text_area("Paste your resume here")

job_description = st.text_area("Paste the job description here")

if st.button("Analyze"):
    if resume and job_description:
        resume_words = set(resume.lower().split())
        job_words = set(job_description.lower().split())

        matching_words = resume_words.intersection(job_words)

        match_percentage = (len(matching_words) / len(job_words)) * 100

        st.success(f"Resume Match: {match_percentage:.1f}%")

    else:
        st.warning("Please enter both your resume and the job description.")