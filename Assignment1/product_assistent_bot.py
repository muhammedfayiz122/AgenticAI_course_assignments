from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import os
from typing import Optional

load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGSMITH_API_KEY")
os.environ["LANGSMITH_PROJECT"] = os.getenv("LANGSMITH_PROJECT")
os.environ["LANGCHAIN_TRACKING_V2"] = "true"

class ProductDetails(BaseModel):
    """
    pydantic model
    """
    product_name: str = Field(description="product name"),
    product_details: str = Field(description="product details"),
    tentative_price: Optional[float] = Field(description="product tentative price in USD")

output_parser = JsonOutputParser(pydantic_object=ProductDetails)

model = ChatGroq(model="compound-beta-mini")

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are an e-commerce AI assistant. When a user asks you about products, you must provide the information in a json format like product name , products details and its tentative price"),
        ("user","{input}")
    ]
)

chain = prompt|model|output_parser
while 1:
    try:
        response = chain.invoke({"input":input("user : ")})
        print(f"AI   :{response}")
    except Exception as e:
        print(e)