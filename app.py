import streamlit as st
import google.generativeai as genai 
import os 
from dotenv import load_dotenv 
import json 
import PyPDF2 as pdf


load_dotenv()

genai.configure(api_key="AIzaSyAaJY5e6aMq9o71ImCUyVfssW9WoEJ4OqM")

def get_gemini_response(input):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input)
    
    return response.text


def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        page = reader.pages[page]
        text+=str(page.extract_text())
    return text 

def improve_text_quality(generated_text):
    pass







# streamlit for web application 
# st.title("TalentSync Pro")
st.markdown('<h2 style="color: #27ae60;">TalentSync Pro</h2>', unsafe_allow_html=True)

st.text("Match your resume with ATS Score for Free.")
# st.markdown('<h2 style="color: #27ae60;">Seamless Job Matching, Precision Hiring – Elevate Your Professional Journey</h2>', unsafe_allow_html=True)

job_description = st.text_area("Paste the job description")
uploaded_file = st.file_uploader("Upload Your Resume", type="pdf", help="Please Upload The Pdf Format")

submit = st.button("Submit")

if job_description is None and uploaded_file is None:
    st.text("Please Upload File and Test")

if submit:
    if uploaded_file is not None:

        text = input_pdf_text(uploaded_file)
        
        input_prompt = f"""
        Hey, Act Like a skilled or very experienced ATS(Application Tracking System) with a deep understanding of the tech field,
        software engineering, full-stack engineering, and frontend engineering. 
        Your Task is to evaluate the resume based on the given job description. 
        Now Your work is to match the resume with the job description and give the accuracy of the match and what keywords are missing in the resume that are mentioned in the job description. 
        Please avoid providing random answers; I expect responses based on the match between the job description and the resume.

        resume: {text}
        description : {job_description}

        I want the response in one single string having the structure:
        [
            'ATS Score: "%",
            "Missing Keywords" : "",
            "Profile Summary" : ""
        ]
        """


        response = get_gemini_response(input_prompt)
        st.markdown('<p1 style="color: #27ae60;">Done</p1>', unsafe_allow_html=True)
        st.subheader(response)
        