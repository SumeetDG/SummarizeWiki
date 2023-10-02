import streamlit as st
from scrape import scraper
from process_text import summarize
from create_doc import create
from docx import Document

st.title("Summarize Wikipedia")

st.write("Enter the URL")
url= st.text_input("Enter the URL here:")

done=st.button("Summarize",key="1")

#st.secrets.toml("secrets.toml")
api_key1 = st.secrets["api_keys"]["api_key1"]
api_key2 = st.secrets["api_keys"]["api_key2"]

if done:
    data,title=scraper(url)
    
    summarized_data=summarize(data,api_key1,api_key2)

    doc=create(title,summarized_data)

    st.write("Document Created")
    st.write("Click on the button Below to Download the summarized webpage in Docx format")
    st.download_button(
            label="Click here to Download",
            data=doc,
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            file_name="wikipedia.docx"
        )
