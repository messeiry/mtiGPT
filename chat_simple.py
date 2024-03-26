import streamlit as st
import random
import time
import ollama
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma


### Embedding and retrival
# Create Ollama embeddings and vector store
embeddings = OllamaEmbeddings(model="mistral")
persist_directory = "vectorstores"  # Same as original file
vectorstore = Chroma(persist_directory=persist_directory, embedding_function=embeddings)
#check_db_search = vectorstore.similarity_search("who is mohamed elmesseiry")
#print(check_db_search)
# Create the retriever
retriever = vectorstore.as_retriever()

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

# Define the Ollama LLM function
# def ollama_llm(question, context):
#     formatted_prompt = f"Question: {question}\n\nContext: {context}"
#     response = ollama.chat(model='llama2', 
#                            messages=[{'role': 'user', 'content': formatted_prompt}])
#     return response['message']['content']

# Define the RAG chain
def rag_chain(model, question):
    retrieved_docs = retriever.invoke(question)
    formatted_context = format_docs(retrieved_docs)
    print(f'Documents available : { retrieved_docs }')
    formatted_prompt = f"Question: {question}\n\nContext: {formatted_context}"
    #response = ollama.chat(model='llama2', messages=[{'role': 'user', 'content': formatted_prompt}])
    #return response['message']['content']
    
    # Stage 2: Stream the LLMs response
    llm_stream = ollama.chat( 
        model=model, 
        messages=[{'role': 'user', 'content': formatted_prompt}],
        stream=True 
    )
    for chunk in llm_stream:
        yield chunk['message']['content'] 
        
# Use the RAG chain
#result = rag_chain("Who is mohamed elmesseiry?")
#print(result)


def get_response(selected_llm, question):
  stream = ollama.chat( 
      model= selected_llm,
      messages=[{'role': 'user', 'content': question}],
      stream=True,
  )
  for chunk in stream:
    print(chunk['message']['content'], end='', flush=True)
    yield chunk['message']['content']
  

## GUI 

selected_llm = "llama2"
welcome_msg = "Hi, Im Groot 👋"

st.title("🥷🏻 mtiGPT 1.0 !")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?", key="real_chat_input"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        #response = st.write_stream(response_generator())
        #response = st.write_stream(get_response(selected_llm, prompt))
        response = st.write_stream(rag_chain(selected_llm, prompt))
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})

