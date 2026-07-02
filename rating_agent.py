from langgraph.graph import StateGraph, START, END
from schemas import MovieState
def filter_top_rated(state):

    movies = state.get("genre_movies",) or []

    seen = set()
    top = [
        movie for movie in movies
        if movie.get("vite_average",0)>=8
    ]

    for movie in movies:
        if movie.get("vote_average", 0) >= 8:
            movie_id = movie.get("id")
            if movie_id not in seen:
                top.append(movie)
                seen.add(movie_id)

    return {
        "top_rated_movies": top
    }
graph = StateGraph(MovieState)

graph.add_node("filter_top_rated", filter_top_rated)

graph.add_edge(START, "filter_top_rated")
graph.add_edge("filter_top_rated", END)

rating_graph = graph.compile()