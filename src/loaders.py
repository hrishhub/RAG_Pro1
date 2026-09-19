from pathlib import Path
from pypdf import PdfReader


def load_txt(file_path: str) -> str:
 
    path = Path(file_path)

    with open(path, "r", encoding="utf-8") as file:
        return file.read()


def load_pdf(file_path: str) -> str:
   
    reader = PdfReader(file_path)

    pages = []

    for page in reader.pages:
        text = page.extract_text()

        if text:
            pages.append(text)

    return "\n".join(pages)


def load_document(file_path: str) -> str:
    

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    extension = path.suffix.lower()

    if extension == ".txt":
        return load_txt(file_path)

    elif extension == ".pdf":
        return load_pdf(file_path)

    else:
        raise ValueError(
            f"Unsupported file type: {extension}. "
            "Only .txt and .pdf are supported."
        )