from langgraph.graph import StateGraph, START, END
from schemas import MovieState
from tools import get_movies_by_genre
def detect_genre(state):
    query = (state.get("user_query") or "").lower()

    if "action" in query:
        genre = "Action"
    elif "comedy" in query:
        genre = "Comedy"
    elif "horror" in query:
        genre = "Horror"
    elif "romance" in query:
        genre = "Romance"
    else:
        genre = "Action"

    movies = get_movies_by_genre(genre)

    return {
        "genre": genre,
        "genre_movies": movies[:5]
    }
    print("Node is running")

    query = state["user_query"].lower()

    if "action" in query:
        genre = "Action"
    elif "comedy" in query:
        genre = "Comedy"
    elif "horror" in query:
        genre = "Horror"
    elif "romance" in query:
        genre = "Romance"
    else:
        genre = "Action"

    movies = get_movies_by_genre(genre)

    return {
        "genre": genre,
        "genre_movies": movies[:5]
    }
    
    if "telugu" in query:
       language = "te"
    elif "hindi" in query:
       language = "hi"
    elif "english" in query:
       language = "en"
    else:
       language = None
    
    
graph = StateGraph(MovieState)

graph.add_node("detect_genre", detect_genre)

graph.add_edge(START, "detect_genre")
graph.add_edge("detect_genre", END)

genre_graph = graph.compile()