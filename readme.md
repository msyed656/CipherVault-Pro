# 🔐 CipherVault Pro

CipherVault Pro is a modern AES-powered file and text encryption platform built with Python and Streamlit.

Live Demo: https://ciphervault-pro-vgjzerqys4sgxr78n3a8ak.streamlit.app/

This project allows users to:
- Encrypt and decrypt text
- Encrypt and decrypt files
- Upload PDFs, DOCX files, TXT files, and images
- Extract readable text from decrypted PDFs and DOCX files
- Download restored decrypted files securely

---

# 🚀 Features

✅ AES/Fernet encryption  
✅ Multi-file support  
✅ PDF text extraction  
✅ DOCX text extraction  
✅ Image preview support  
✅ Download decrypted files  
✅ Modern professional UI  
✅ Streamlit web application  

---

# 🛠️ Technologies Used

- Python
- Streamlit
- Cryptography (Fernet/AES)
- PyPDF
- Python-Docx
- Pillow

---

# 🔑 Important Security Note

The secret encryption key is required to decrypt encrypted data.

If the key is lost:
- encrypted files cannot be recovered
- there is no reset system
- decryption permanently fails

---

# ▶️ How To Run The Project

## Install dependencies

```bash
pip install -r requirements.txt
```

## Run the app

```bash
python -m streamlit run app.py
```

---

# 📂 Supported File Types

| File Type | Supported |
|---|---|
| TXT | ✅ |
| PDF | ✅ |
| DOCX | ✅ |
| PNG/JPG | ✅ |
| CSV | ✅ |
| JSON | ✅ |

---

# 📸 Project Preview

## 📸 Project Preview

![CipherVault Screenshot](assets/ciphervault.png)           

---

# 👨‍💻 Author

Mohammad Syed