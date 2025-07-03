from langchain_google_genai import ChatGoogleGenerativeAI

def model_loader():
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
    return llm


