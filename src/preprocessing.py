import os

from pdf_loader import extract_pdf_text
from text_cleaner import clean_text
from document_builder import build_document
from validator import validate_document
from json_writer import save_documents


RESUME_FOLDER = "../resumes"
OUTPUT_FILE = "../processed_data/resumes.json"


def main():

    documents = []

    for file_name in os.listdir(RESUME_FOLDER):

        if not file_name.lower().endswith(".pdf"):
            continue

        file_path = os.path.join(RESUME_FOLDER, file_name)

        print(f"Processing : {file_name}")

        text = extract_pdf_text(file_path)

        clean_resume = clean_text(text)

        document = build_document(
            doc_id=len(documents) + 1,
            file_name=file_name,
            text=clean_resume
        )

        if validate_document(document):
            documents.append(document)

    save_documents(documents, OUTPUT_FILE)


if __name__ == "__main__":
    main()