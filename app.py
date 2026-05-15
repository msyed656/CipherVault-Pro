import streamlit as st
import aes_tools


# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(

    page_title="CipherVault Pro",

    page_icon="🔐",

    layout="wide"

)

# =====================================================
# PROFESSIONAL CLEAN UI THEME
# =====================================================
st.markdown("""
<style>

/* =====================================================
MAIN APP
===================================================== */

.stApp {
    background-color: #f8fafc;
    color: #0f172a;
    font-family: "Segoe UI", sans-serif;
}


/* =====================================================
REMOVE TOP HEADER
===================================================== */

header[data-testid="stHeader"] {
    background: transparent !important;
}


/* =====================================================
MAIN CONTENT AREA
===================================================== */

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 1100px;
}


/* =====================================================
HEADINGS
===================================================== */

h1 {
    color: #0f172a !important;
    font-weight: 800 !important;
}

h2, h3 {
    color: #1e293b !important;
    font-weight: 700 !important;
}


/* =====================================================
GENERAL TEXT
===================================================== */

p,
label,
span,
div {
    color: #0f172a !important;
}


/* =====================================================
SIDEBAR
===================================================== */

section[data-testid="stSidebar"] {

    background-color: #ffffff !important;

    border-right: 1px solid #e2e8f0 !important;
}

section[data-testid="stSidebar"] * {

    color: #0f172a !important;
}


/* =====================================================
PROFESSIONAL BUTTONS
===================================================== */

.stButton > button {

    background-color: #2563eb !important;

    color: #ffffff !important;

    border: none !important;

    border-radius: 10px !important;

    padding: 0.7rem 1.2rem !important;

    font-weight: 600 !important;

    font-size: 15px !important;

    transition: 0.2s ease-in-out !important;

    box-shadow:
    0 2px 8px rgba(37, 99, 235, 0.15) !important;
}


/* BUTTON HOVER */
.stButton > button:hover {

    background-color: #1d4ed8 !important;

    color: #ffffff !important;

    transform: translateY(-1px);

    box-shadow:
    0 4px 12px rgba(37, 99, 235, 0.25) !important;
}


/* BUTTON TEXT */
.stButton > button * {

    color: #ffffff !important;
}


/* =====================================================
DOWNLOAD BUTTONS
===================================================== */

.stDownloadButton > button {

    background-color: #16a34a !important;

    color: #ffffff !important;

    border: none !important;

    border-radius: 10px !important;

    padding: 0.7rem 1.2rem !important;

    font-weight: 600 !important;
}

.stDownloadButton > button * {

    color: #ffffff !important;
}


/* =====================================================
TEXT AREAS
===================================================== */

textarea {

    background-color: #ffffff !important;

    color: #0f172a !important;

    border: 1px solid #cbd5e1 !important;

    border-radius: 10px !important;
}


/* =====================================================
INPUT BOXES
===================================================== */

input {

    background-color: #ffffff !important;

    color: #0f172a !important;

    border: 1px solid #cbd5e1 !important;
}


/* =====================================================
RADIO BUTTON TEXT
===================================================== */

div[role="radiogroup"] label,
div[role="radiogroup"] span,
div[role="radiogroup"] p {

    color: #0f172a !important;
}


/* =====================================================
FILE UPLOADER
===================================================== */

[data-testid="stFileUploader"] {

    background-color: #ffffff !important;

    border: 1px solid #cbd5e1 !important;

    border-radius: 14px !important;

    padding: 1rem !important;
}

[data-testid="stFileUploader"] * {

    color: #0f172a !important;
}


/* =====================================================
CODE BLOCKS / SECRET KEY
===================================================== */

pre {

    background-color: #ffffff !important;

    color: #000000 !important;

    border: 1px solid #cbd5e1 !important;

    border-radius: 12px !important;

    padding: 12px !important;
}

code {

    background-color: #ffffff !important;

    color: #000000 !important;
}

pre * {

    color: #000000 !important;
}

code * {

    color: #000000 !important;
}


/* =====================================================
ALERT BOXES
===================================================== */

[data-testid="stAlert"] {

    border-radius: 12px !important;
}

[data-testid="stAlert"] * {

    color: #0f172a !important;
}


/* =====================================================
EXPANDERS
===================================================== */

.streamlit-expanderHeader {

    background-color: #ffffff !important;

    color: #0f172a !important;

    border-radius: 10px !important;
}


/* =====================================================
CLEAN SPACING
===================================================== */

[data-testid="stVerticalBlock"] {

    gap: 1rem;
}

</style>
""", unsafe_allow_html=True)




# =====================================================
# CREATE SECRET KEY
# =====================================================

if "key" not in st.session_state:

    st.session_state.key = aes_tools.generate_key()





# =====================================================
# HERO SECTION
# =====================================================

st.markdown("""

### AES-powered encryption for text, PDFs, DOCX files, images, and more.

Protect your files with a secret key, decrypt them safely, preview readable content, and download restored files.
""")

st.warning("""
⚠️ Save your secret key.

If you lose this key, your encrypted files cannot be recovered.
There is no reset button. Treat it like the password to a vault.
""")


# =====================================================
# Side Bar
# =====================================================

st.sidebar.title("🔐 CipherVault")
st.sidebar.write("Secure AES file encryption")
st.sidebar.success("System Online")

# =====================================================
# WARNING MESSAGE
# =====================================================

st.warning("""

⚠️ IMPORTANT — SAVE YOUR SECRET KEY

Your secret key is REQUIRED to decrypt your encrypted files.

If you lose the key:
- your encrypted files CANNOT be recovered
- there is NO reset system
- decryption will permanently fail

Treat your key like a vault password.

""")


# =====================================================
# SHOW SECRET KEY
# =====================================================

st.subheader("🔑 Your Secret Encryption Key")

st.code(

    st.session_state.key.decode()

)


# =====================================================
# MODE SELECTION
# =====================================================

mode = st.radio(

    "Choose Encryption Mode",

    ["Text", "File"]

)


# =====================================================
# TEXT MODE
# =====================================================

if mode == "Text":

    st.subheader("📝 Text Encryption")

    text = st.text_area(

        "Enter your text"

    )


    # =================================================
    # ENCRYPT TEXT
    # =================================================

    if st.button(

        "Encrypt Text",

        key="encrypt_text_btn"

    ):

        encrypted = aes_tools.encrypt_text(

            text,

            st.session_state.key

        )

        st.session_state.encrypted_text = encrypted

        st.success("✅ Text Encrypted Successfully")

        st.code(encrypted)


    # =================================================
    # DECRYPT TEXT
    # =================================================

    if st.button(

        "Decrypt Text",

        key="decrypt_text_btn"

    ):

        if "encrypted_text" not in st.session_state:

            st.error(

                "Please encrypt text first"

            )

        else:

            decrypted = aes_tools.decrypt_text(

                st.session_state.encrypted_text,

                st.session_state.key

            )

            if decrypted is None:

                st.error(

                    "❌ Invalid key or encrypted data"

                )

            else:

                st.success(

                    "✅ Text Decrypted Successfully"

                )

                try:

                    st.code(

                        decrypted.decode("utf-8")

                    )

                except:

                    st.code(

                        decrypted.decode(

                            "latin-1",

                            errors="ignore"

                        )

                    )


# =====================================================
# FILE MODE
# =====================================================

else:

    st.subheader("📁 File Encryption")

    uploaded_file = st.file_uploader(

        "Upload a file"

    )


    # =================================================
    # SAVE FILE DATA
    # =================================================

    if uploaded_file is not None:

        st.session_state.file_data = (

            uploaded_file.read()

        )

        st.session_state.file_name = (

            uploaded_file.name

        )

        st.success(

            "✅ File uploaded successfully"

        )

        st.write("📄 File Name:")

        st.code(

            st.session_state.file_name

        )

    else:

        st.info(

            "Please upload a file"

        )


    # =================================================
    # ENCRYPT FILE
    # =================================================

    if st.button(

        "Encrypt File",

        key="encrypt_file_btn"

    ):

        if "file_data" not in st.session_state:

            st.error(

                "Please upload a file first"

            )

        else:

            encrypted = aes_tools.encrypt_text(

                st.session_state.file_data,

                st.session_state.key

            )

            st.session_state.encrypted_data = encrypted

            st.success(

                "✅ File Encrypted Successfully"

            )

            st.code(

                encrypted[:500]

            )


    # =================================================
    # DECRYPT FILE
    # =================================================

    if st.button(

        "Decrypt File",

        key="decrypt_file_btn"

    ):

        if "encrypted_data" not in st.session_state:

            st.error(

                "Please encrypt a file first"

            )

        else:

            decrypted = aes_tools.decrypt_text(

                st.session_state.encrypted_data,

                st.session_state.key

            )

            if decrypted is None:

                st.error(

                    "❌ Wrong key or invalid data"

                )

            else:

                st.success(

                    "✅ File Decrypted Successfully"

                )

                file_name = (

                    st.session_state.file_name.lower()

                )


                # =====================================
                # SHOW RAW DECRYPTED DATA
                # =====================================

                st.subheader(

                    "🔓 Raw Decrypted Data"

                )

                try:

                    st.code(

                        decrypted.decode("utf-8")

                    )

                except:

                    st.write(

                        decrypted[:500]

                    )


                # =====================================
                # PDF FILES
                # =====================================

                if file_name.endswith(".pdf"):

                    st.subheader(

                        "📄 Extracted PDF Text"

                    )

                    pdf_text = (

                        aes_tools.extract_pdf_text(

                            decrypted

                        )

                    )

                    st.text_area(

                        "PDF Content",

                        pdf_text,

                        height=300

                    )


                # =====================================
                # DOCX FILES
                # =====================================

                elif file_name.endswith(".docx"):

                    st.subheader(

                        "📝 Extracted DOCX Text"

                    )

                    docx_text = (

                        aes_tools.extract_docx_text(

                            decrypted

                        )

                    )

                    st.text_area(

                        "DOCX Content",

                        docx_text,

                        height=300

                    )


                # =====================================
                # TXT FILES
                # =====================================

                elif file_name.endswith(".txt"):

                    st.subheader(

                        "📄 Text File Content"

                    )

                    try:

                        text = decrypted.decode(

                            "utf-8"

                        )

                    except:

                        text = decrypted.decode(

                            "latin-1",

                            errors="ignore"

                        )

                    st.text_area(

                        "TXT Content",

                        text,

                        height=300

                    )


                # =====================================
                # IMAGE FILES
                # =====================================

                elif (

                    file_name.endswith(".png")

                    or

                    file_name.endswith(".jpg")

                    or

                    file_name.endswith(".jpeg")

                ):

                    st.subheader(

                        "🖼️ Decrypted Image"

                    )

                    st.image(

                        decrypted

                    )


                # =====================================
                # DOWNLOAD DECRYPTED FILE
                # =====================================

                st.download_button(

                    label="⬇ Download Decrypted File",

                    data=decrypted,

                    file_name=st.session_state.file_name,

                    mime="application/octet-stream"

                )