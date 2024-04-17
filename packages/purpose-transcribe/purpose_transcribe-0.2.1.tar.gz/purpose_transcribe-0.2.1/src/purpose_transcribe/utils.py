# src/utils.py
import zipfile
import tempfile

def extract_zip(input_zip, extract_to):
    """Extracts the contents of a zip file to a specified directory."""
    with zipfile.ZipFile(input_zip, "r") as zip_ref:
        zip_ref.extractall(extract_to)