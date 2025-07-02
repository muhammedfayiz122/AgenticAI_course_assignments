
from langgraph.graph import StateGraph, MessagesState, END, START
from langgraph.prebuilt import ToolNode, tools_condition


class GraphBuilder():
    def __init__(self):        
        self.graph = None
    
    def agent_function(self,state: MessagesState):
        """Main agent function"""
        pass

    def build_graph(self):
        graph_builder=StateGraph(MessagesState)
        graph_builder.add_node("agent", self.agent_function)
        graph_builder.add_node("tools", self.agent_function)
        graph_builder.add_edge(START,"agent")
        graph_builder.add_conditional_edges("agent",tools_condition)
        graph_builder.add_edge("tools","agent")
        graph_builder.add_edge("agent",END)
        self.graph = graph_builder.compile()
        return self.graph
        
    def __call__(self):
        return self.build_graph()
    
if __name__ == "__main__":
    g = GraphBuilder()
    g()