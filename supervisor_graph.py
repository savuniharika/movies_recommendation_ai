from langgraph.graph import StateGraph, START, END
from schemas import MovieState

from genre_agent import detect_genre
from rating_agent import filter_top_rated


# --- nodes ---
def genre_node(state):
    return detect_genre(state)

def rating_node(state):
    return filter_top_rated(state)

def format_output(state):
    return {
        "final_output": {
            "genre": state.get("genre"),
            "language": state.get("language"),
            "movies": [
                movie.get("title")
                for movie in state.get("top_rated_movies", [])
            ]
        }
    }


# --- build graph ---
graph = StateGraph(MovieState)

graph.add_node("genre_agent", genre_node)
graph.add_node("rating_agent", rating_node)
graph.add_node("format_output", format_output)

graph.add_edge(START, "genre_agent")
graph.add_edge("genre_agent", "rating_agent")
graph.add_edge("rating_agent", "format_output")
graph.add_edge("format_output", END)

supervisor_graph = graph.compile()