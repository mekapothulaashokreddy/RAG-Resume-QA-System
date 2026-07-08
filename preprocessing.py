import os
import json
import fitz

resume_folder = "resumes"

documents = []

for file_name in os.listdir(resume_folder):

    file_path = os.path.join(resume_folder, file_name)

    if file_name.lower().endswith(".pdf"):

        pdf = fitz.open(file_path)

        text = ""

        for page in pdf:
            text += page.get_text()

        pdf.close()

        document = {
            "id": len(documents) + 1,
            "candidate_name": os.path.splitext(file_name)[0],
            "file_name": file_name,
            "content": text
        }

        documents.append(document)

output_path = "processed_data/resumes.json"

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(documents, f, indent=4, ensure_ascii=False)

print(f"{len(documents)} resumes saved successfully.")
print(f"Output File : {output_path}")