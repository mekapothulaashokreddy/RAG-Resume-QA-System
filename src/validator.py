def validate_document(document):
    """
    Validate one resume document.
    """

    if not document["candidate_name"].strip():
        return False

    if not document["content"].strip():
        return False

    return True