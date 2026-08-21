import numpy as np
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()


chat_model = ChatGoogleGenerativeAI(
    model='gemini-3.7-flash',
    temperature=1.0,

    max_tokens=None, 
)

chat_history = [
    SystemMessage(content='You are a helpful AI assistant')
]

print("Chat started! Type 'exit' to stop.\n")

while True:
    user_input = input("You: ")
    
    if user_input.strip().lower() == "exit":
        break
        
    chat_history.append(HumanMessage(content=user_input))
    
    result = chat_model.invoke(chat_history)
    
    chat_history.append(AIMessage(content=result.content))
    print(f"AI: {result.text}\n")
    
print('Sonam its Done Bro')
