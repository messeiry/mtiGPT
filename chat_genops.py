# LangChain supports many other chat models. Here, we're using Ollama
from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from langchain.memory import ChatMessageHistory




import streamlit as st

selected_llm = "llama2"

llm = ChatOllama(model=selected_llm)

history = ChatMessageHistory()

prompt = ChatPromptTemplate.from_template(
    "Your name: Abd-El-Gabar, role: {role}, "
    "system: As a GenOps agent, you expedite DevOps engineers, "
    "You are responding to: {question}, "
    "Decorate your responses with emojis,"
)

chain = prompt | llm | StrOutputParser()

#print(chain.invoke({"role": "assistant", "question": "what is your name?"}))

def get_response(role, question):
    
    history.add_message(question)
    
    stream = chain.stream( 
        {"role": role, "question": question},
    )
    for chunk in stream:
        #print(chunk, end='', flush=True)
        yield chunk
    
    
# GUI
  


st.set_page_config(page_title="🧞 GenOps Assistant")

st.title("🧞 GenOps Assistant")
# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"], avatar="🧙‍♂️" if message["role"] == "user" else "🧞"):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?", key="real_chat_input"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message in chat message container
    with st.chat_message("user", avatar="🧙‍♂️"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant", avatar="🧞"):
        #response = st.write_stream(response_generator())
        #response = st.write_stream(get_response(selected_llm, prompt))
        response = st.write_stream(get_response("assistant", prompt))
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
        

    print(history.messages)