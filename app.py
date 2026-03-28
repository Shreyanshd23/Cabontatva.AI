import streamlit as st

st.set_page_config(page_title="NotebookLM App")

st.title(" My AI Research Assistant")

st.write("This app uses NotebookLM for answering questions from documents.")

#  IMPORTANT: paste your NotebookLM share link below
notebook_url = "https://notebooklm.google.com/notebook/81d4c165-789c-44a0-b556-7c1661f54c44?authuser=1"

st.link_button("Open Notebook", notebook_url)

st.markdown("---")

st.subheader("Features")
st.write("""
- Upload documents in NotebookLM  
- Ask questions  
- Get AI-powered answers  
""")

st.subheader("About")
st.write("Built using Streamlit + NotebookLM")