from typing import TypedDict, List, Dict, Any

class MovieState(TypedDict):
    user_query: str
    genre: str
    language: str
    genre_movies: List[Dict[str, Any]]
    top_rated_movies: List[Dict[str, Any]]
    similar_movies: List[Dict[str, Any]]
    final_recommendations: List[Dict[str, Any]]