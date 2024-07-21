import streamlit as st
import os
from litellm import completion
import fitz  # PyMuPDF
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Ensure that the environment variable is set
os.environ["GEMINI_API_KEY"] = os.getenv('GEMINI_API_KEY')

# Function to process grammar checking and rephrasing using Gemini API
def process_text(text, mode):
    if mode == "Grammar Check":
        prompt = f"Please correct the grammar of the following text and explain the changes made:\n\n{text}"
    elif mode == "Rephrase":
        prompt = f"Please rephrase the following text: {text}"
    
    response = completion(
        model="gemini/gemini-pro", 
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response.get('choices', [{}])[0].get('message', {}).get('content', 'No response')

# Function to extract text from PDF
def extract_text_from_pdf(file):
    pdf_document = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        text += page.get_text()
    return text

# Set up Streamlit app
st.set_page_config(page_title="TextTune", page_icon="📝", layout="wide")

st.title("TextTune")

# Add some styling
st.markdown("""
    <style>
        .main {
            background-color: #000000;
            color: #ffffff;
        }
        .stApp {
            background-color: #000000;
            color: #ffffff;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-size: 18px;
            border-radius: 10px;
            padding: 10px;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        .stTextInput>div>div>input {
            border-radius: 10px;
            background-color: #333333;
            color: #ffffff;
        }
        .stTextArea>div>textarea {
            border-radius: 10px;
            background-color: #333333;
            color: #ffffff;
        }
        .stRadio>div>label>div {
            color: #ffffff;
        }
    </style>
    """, unsafe_allow_html=True)

# Radio button to choose input method
input_method = st.radio("Choose input method:", ["Manual Input", "Upload PDF"], index=0, help="Select the method you prefer to input your text.")

# Input section based on the chosen method
if input_method == "Manual Input":
    st.header("Manual Input")
    st.write("Enter your text in the box below and choose the mode to either check grammar or rephrase the text.")
    text_input = st.text_area("Enter text:", "", height=200)
    mode = st.radio("Select mode:", ["Grammar Check", "Rephrase"], key="common_mode")
    if st.button("Submit", key="manual_submit"):
        if text_input:
            with st.spinner("Processing..."):
                response = process_text(text_input, mode)
                st.write("**Result:**")
                st.write(response)
        else:
            st.error("Please enter some text to process.")

elif input_method == "Upload PDF":
    st.header("Upload PDF")
    st.write("Upload your PDF file below. The text will be extracted, and you can then choose to check the grammar or rephrase it.")
    pdf_file = st.file_uploader("Choose a PDF file", type="pdf")
    if pdf_file:
        with st.spinner("Extracting text from PDF..."):
            text_from_pdf = extract_text_from_pdf(pdf_file)
            st.text_area("Extracted text:", text_from_pdf, height=300, key="pdf_text_area")
            mode = st.radio("Select mode for PDF:", ["Grammar Check", "Rephrase"], key="common_mode_pdf")
            if st.button("Submit", key="pdf_submit"):
                if text_from_pdf:
                    with st.spinner("Processing..."):
                        response = process_text(text_from_pdf, mode)
                        st.write("**Result:**")
                        st.write(response)
                else:
                    st.error("No text extracted from the PDF.")
