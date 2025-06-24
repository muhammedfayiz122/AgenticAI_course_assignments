from IPython.display import Image, display

def display_graph(graph):
    png = graph.get_graph().draw_mermaid_png()
    display(Image(png))