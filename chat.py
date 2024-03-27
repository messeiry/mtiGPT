from langchain_community.llms import Ollama

from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

prompt = "Why is the sky blue?"


llm = Ollama(
    model="llama2", 
    callback_manager=CallbackManager([StreamingStdOutCallbackHandler()])
)

llm.invoke(prompt)