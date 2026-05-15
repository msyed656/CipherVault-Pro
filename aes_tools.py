from cryptography.fernet import Fernet, InvalidToken
from pypdf import PdfReader
from docx import Document
import io


# =====================================================
# GENERATE SECRET KEY
# =====================================================
def generate_key():

    return Fernet.generate_key()


# =====================================================
# ENCRYPT DATA
# =====================================================
def encrypt_text(data, key):

    cipher = Fernet(key)

    # If user enters text,
    # convert it into bytes
    if isinstance(data, str):

        data = data.encode("utf-8")

    # Encrypt bytes
    encrypted = cipher.encrypt(data)

    # Convert encrypted bytes into string
    # so Streamlit can display it
    return encrypted.decode("utf-8")


# =====================================================
# DECRYPT DATA
# =====================================================
def decrypt_text(data, key):

    cipher = Fernet(key)

    try:

        # Convert encrypted text back into bytes
        decrypted = cipher.decrypt(data.encode("utf-8"))

        # Return RAW BYTES
        return decrypted

    except InvalidToken:

        return None


# =====================================================
# EXTRACT PDF TEXT
# =====================================================
def extract_pdf_text(pdf_bytes):

    pdf_file = io.BytesIO(pdf_bytes)

    reader = PdfReader(pdf_file)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:

            text += page_text + "\n"

    return text


# =====================================================
# EXTRACT DOCX TEXT
# =====================================================
def extract_docx_text(docx_bytes):

    file = io.BytesIO(docx_bytes)

    doc = Document(file)

    text = ""

    for para in doc.paragraphs:

        text += para.text + "\n"

    return text