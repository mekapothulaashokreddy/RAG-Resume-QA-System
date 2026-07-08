# 📄 RAG Resume Question Answering System

An AI-powered Resume Question Answering System built using **Retrieval-Augmented Generation (RAG)**. This application allows users to upload multiple resumes, store them in a vector database, and ask natural language questions to retrieve candidate-specific information.

---

## 🚀 Project Overview

This project combines semantic search and Large Language Models (LLMs) to answer questions from a collection of resumes.

Instead of manually searching through resumes, users can simply ask questions such as:

- What are Ashok Reddy's skills?
- Who has experience in Machine Learning?
- Which candidate worked on Driver Drowsiness Detection?
- Compare two candidates based on their skills.

The application retrieves the most relevant resume using vector embeddings and generates accurate answers using an LLM.

---

## ✨ Features

- Upload multiple PDF resumes
- Extract text from PDF documents
- Clean and preprocess resume data
- Generate sentence embeddings
- Store embeddings in ChromaDB
- Semantic resume retrieval
- AI-powered question answering using OpenRouter LLM
- Modular project architecture
- Easy to extend and maintain

---

## 🛠️ Tech Stack

- Python
- ChromaDB
- Sentence Transformers
- LangChain
- OpenRouter API
- Hugging Face Embeddings
- Streamlit (UI - Coming Soon)

---

## 📂 Project Structure

```text
RAG-Resume-QA-System
│
├── resumes/
├── processed_data/
├── src/
│   ├── pdf_loader.py
│   ├── text_cleaner.py
│   ├── document_builder.py
│   ├── validator.py
│   ├── json_writer.py
│   ├── preprocessing.py
│   ├── ingest.py
│   ├── retriever.py
│   ├── llm.py
│   ├── rag_pipeline.py
│   └── test_llm.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🔄 Project Workflow

```text
PDF Resumes
      │
      ▼
Text Extraction
      │
      ▼
Text Cleaning
      │
      ▼
JSON Generation
      │
      ▼
Embedding Generation
      │
      ▼
ChromaDB Vector Database
      │
      ▼
Semantic Retrieval
      │
      ▼
OpenRouter LLM
      │
      ▼
Final Answer
```

---

## 🚧 Current Status

✅ Resume Preprocessing

✅ ChromaDB Integration

✅ Semantic Search

✅ OpenRouter LLM Integration

✅ End-to-End RAG Pipeline

🔄 Streamlit User Interface (In Progress)

---

## 📌 Future Enhancements

- Resume Upload through UI
- Candidate Comparison
- Skills Filtering
- Resume Ranking
- Chat History
- Deployment on Streamlit Cloud

---

## 👨‍💻 Author

**Mekapothula Ashok Reddy**

GitHub:
https://github.com/mekapothulaashokreddy

LinkedIn:
https://www.linkedin.com/in/mekapothula-ashok-reddy

---

⭐ If you found this project useful, consider giving it a star.
