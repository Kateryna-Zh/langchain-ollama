from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOllama(model="llama3.2")
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "Explain LangChain in simple terms.")
    ])
chain = prompt | llm
print(chain.invoke({"question": "Explain LangChain in simple terms."}))