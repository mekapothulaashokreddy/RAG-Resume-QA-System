import os
import fitz
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import Docx2txtLoader
from langchain_core.documents import Document
resume_folder = "resumes"
documents = []
for file_name in os.listdir(resume_folder):
    file_path = os.path.join(resume_folder,file_name)

    if file_name.lower().endswith(".pdf"):
        pdf = fitz.open(file_path)
        text = ""
        for page in pdf:
            text+=page.get_text()
        pdf.close()
        print(text[:200])
    elif file_name.lower().endswith(".docx"):
        print(f"{file_name} is a DOCX")
doc = fitz.open(file_path)
doc = Document(file_path)