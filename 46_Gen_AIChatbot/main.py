import streamlit as st
import pdfplumber
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate


OPENAI_API_KEY="openai_api_key_here.."

st.header("My First ChatBot")

with st.sidebar:
    
    st.title("Your Document")
    my_file = st.file_uploader("Upload a pdf file and start asking questions...", type='pdf')
    
##Extract content from pdf ( and chunk it)
if my_file is not None:
    #extract text from it
    with pdfplumber.open(my_file) as pdf:
        text = ""
        for page in pdf.pages:
            text +=page.extract_text() + "\n"
    
    # st.write(text)
    
    # split text into chunks
    text_spliter = RecursiveCharacterTextSplitter(
        separators=['\n\n', '\n', '. ', " ", ""],
        chunk_size=1000,
        chunk_overlap=200
    )
    
    chunks = text_spliter.split_text(text)
    # st.write(chunks)
    
    
    #generating embedding
    embedings = OpenAIEmbeddings(
        model="text-embedding-3-small",
        openai_api_key=OPENAI_API_KEY,
        
    )
    
    # store embedding into vector db..
    vector_store = FAISS.from_texts(chunks, embedings)
    
    
    #get user question
    user_question = st.text_input("Type your question here...")
    
    
    #generate answer..
    # question -> embedding -> similarity_search -> result to llm -> response
    def format_docs(docs):
        return "\n\n".join([doc.page_content for doc in docs])

    retriver = vector_store.as_retriever(
        search_type= 'mmr',
        search_kwargs={'k':4}
    )
    # define LLM and prompts
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temprature=0.3,
        max_tokens =1000,
        openai_api_key=OPENAI_API_KEY
    )
    
    #provide the prompts
    prompt = ChatPromptTemplate.from_messages([
        ("system",
        "You are a helpful assistant answering questions about a PDF document.\n\n"
        "Guidelines:\n"
        "1. Provide complete, well-explained answers using the context below.\n"
        "2. Include relevant details, numbers, and explanations to give a thorough response.\n"
        "3. If the context mentions related information, include it to give fuller picture.\n"
        "4. Only use information from the provided context - do not use outside knowledge.\n"
        "5. Summarize long information, ideally in bullets where needed\n"
        "6. If the information is not in the context, say so politely.\n\n"
        "Context:\n{context}"),
        ("human", "{question}")
    ])
    
    
    chain = (
        {
            'context': retriver | format_docs,
            "question":RunnablePassthrough()
        }  # 1. taking the user question and passing to retriver which search vector store and return relavent chunk
        | prompt  # 3 create the prompt 
        | llm  # 2. send  to llm 
        | StrOutputParser()  # 4. get the ouptupt and showing to user...
    )
    
    ## if user give some text...
    if user_question:
        response = chain.invoke(user_question)
        st.write(response)
    


