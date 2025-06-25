def validate_file_type(filename: str) -> bool:
    return filename.endswith((".pptx", ".docx", ".xlsx"))
