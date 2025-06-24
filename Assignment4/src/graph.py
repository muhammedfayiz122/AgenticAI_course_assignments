from langgraph.graph import StateGraph, END
from typing import TypedDict, Sequence, Annotated
from langchain_core.messages import BaseMessage
import operator

class AgentState(TypedDict):
    state: Annotated[Sequence[BaseMessage], operator.add]

class full_graph:
    def __init__(self):
        # exit()
        # print("hello started")
        self.workflow = StateGraph(AgentState)
        self.create_nodes()
        self.add_edges()
        self.set_entry_exit()
        self.compile_graph()
        
    def func1(self, state): 
        print("Searching attractions...")
        return state

    def func2(self, state): 
        print("Getting weather...")
        return state

    def func3(self, state): 
        print("Searching hotels...")
        return state

    def func4(self, state): 
        print("Calculating total cost...")
        return state

    def func5(self, state): 
        print("Converting currency...")
        return state

    def func6(self, state): 
        print("Generating itinerary...")
        return state

    def func7(self, state): 
        print("Creating summary...")
        return state
    
    def create_nodes(self):
        self.workflow.add_node("Search  attractions and activity", self.func1)
        self.workflow.add_node("Search weather forecast", self.func2)
        self.workflow.add_node("Search hotel cost", self.func3)
        self.workflow.add_node("Search total cost", self.func4)
        self.workflow.add_node("Currency conversion", self.func5)
        self.workflow.add_node("Itenary generation", self.func6)
        self.workflow.add_node("Complete Summary", self.func7)

    def add_edges(self):
        self.workflow.add_edge("Search  attractions and activity", "Search weather forecast")
        self.workflow.add_edge("Search weather forecast", "Search hotel cost")
        self.workflow.add_edge("Search hotel cost", "Search total cost")
        self.workflow.add_edge("Search total cost", "Currency conversion")
        self.workflow.add_edge("Currency conversion", "Itenary generation")
        self.workflow.add_edge("Itenary generation", "Complete Summary")

    def set_entry_exit(self):
        self.workflow.set_entry_point("Search  attractions and activity")
        self.workflow.add_edge("Complete Summary", END)

    def compile_graph(self):
        self.graph = self.workflow.compile()

    def return_graph(self):
        return self.graph