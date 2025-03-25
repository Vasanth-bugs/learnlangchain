from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import SystemMessage,HumanMessage,AIMessage
from dotenv import load_dotenv
import os 


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp",api_key=api_key)

chat_history= []
sysmsg = SystemMessage(content='You are a helpful chatbot')
chat_history.append(sysmsg)

while True: 
    query = input("You: ")
    if query.lower() == 'exit': 
        break
    humanmsg = HumanMessage(content=query)
    chat_history.append(humanmsg)
    response = model.invoke(chat_history)  
    print("AI : " + str(response.content)) 
    aimsg = AIMessage(content=response.content)  
    chat_history.append(aimsg)
    # print(chat_history) 