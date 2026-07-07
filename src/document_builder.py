import os


def build_document(doc_id, file_name, text):
    """
    Build one document for one resume.
    """

    document = {
        "id": doc_id,
        "candidate_name": os.path.splitext(file_name)[0],
        "file_name": file_name,
        "content": text
    }

    return document