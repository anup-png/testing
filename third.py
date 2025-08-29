import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os


load_dotenv()


st.title("MCQ Generator")


user_input = st.text_area("Enter your text here:", height=50)

model = ChatGoogleGenerativeAI(
    model = "gemini-2.0-flash",
    google_api_key = os.getenv("GOOGLE_API_KEY")
)

prompt = PromptTemplate(
    template= 'Generate 10 multiple choice question from the following text: {text}',
    input_variables=['text']
)

parser = StrOutputParser()

chain = prompt | model | parser

if st.button("Generate MCQs"):
    if user_input.strip():
        result = chain.invoke({"text": user_input})
        st.write("Generated MCQs:", result)
    else:
        st.write("Please enter some text to generate MCQs.")