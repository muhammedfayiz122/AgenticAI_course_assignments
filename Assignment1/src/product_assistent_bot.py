from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, RootModel, Field
from dotenv import load_dotenv
import os
from typing import Optional, List



class ProductDetails(BaseModel):
    """
    pydantic model to get each attribues as below
    """
    product_name: str = Field(description="product name")
    product_details: list = Field(description="product details")
    tentative_price: Optional[float] = Field(description="product tentative price in USD")

class ProductList(RootModel[List[ProductDetails]]):
    """
    To get all products as in a list
    """
    pass

class ProductAssistant:
    def __init__(self):
        # Loading all Keys
        load_dotenv()
        os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
        os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGSMITH_API_KEY")
        os.environ["LANGSMITH_PROJECT"] = os.getenv("LANGSMITH_PROJECT")
        os.environ["LANGCHAIN_TRACKING_V2"] = "true"

    def llm_chain(self):
        """
        
        """

        # Output format
        output_parser = JsonOutputParser(pydantic_object=ProductList)

        # LLM Model
        model = ChatGroq(model="compound-beta-mini")

        # Prompt
        prompt = ChatPromptTemplate.from_messages(
            [
                ("system","You are an e-commerce AI assistant. When a user asks you about products, you must provide the informations in a json format like product name , products details and its tentative price. You can provide informations about many products from user asked. Follow the output format strictly."),
                ("system", "{format_instructions}"),
                ("user","{input}")
            ]
        ).partial(format_instructions=output_parser.get_format_instructions())

        # LLM chain
        chain = prompt|model|output_parser

        return chain
    
if __name__ == "__main__":
    llmchain = ProductAssistant().llm_chain()
    while 1:
        query = input("Enter product name : ")
        if query:
            response = llmchain.invoke({"input": query})
            if response:
                print(response)