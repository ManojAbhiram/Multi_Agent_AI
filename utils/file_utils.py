import os
import json
from pdfminer.high_level import extract_text

def detect_format(file_path):
    if file_path.endswith(".pdf"):
        return "PDF"
    elif file_path.endswith(".json"):
        return "JSON"
    elif file_path.endswith(".txt") or file_path.endswith(".eml"):
        return "Email"
    return "Unknown"

def read_file(file_path):
    fmt = detect_format(file_path)
    if fmt == "PDF":
        return extract_text(file_path)
    elif fmt == "JSON":
        with open(file_path, 'r') as f:
            return json.load(f)
    elif fmt == "Email":
        with open(file_path, 'r') as f:
            return f.read()
    return None
