import json


def save_documents(documents, output_path):
    """
    Save all documents into a JSON file.
    """

    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(documents, file, indent=4, ensure_ascii=False)

    print(f"\n✅ {len(documents)} resumes saved successfully.")
    print(f"📁 Output File: {output_path}")