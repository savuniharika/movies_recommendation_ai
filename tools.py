import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Read API Key
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

# TMDb Base URL
BASE_URL = "https://api.themoviedb.org/3"

# Genre IDs used by TMDb
GENRE_IDS = {
    "Action": 28,
    "Comedy": 35,
    "Drama": 18,
    "Horror": 27,
    "Romance": 10749,
    "Science Fiction": 878
}


# -----------------------------------
# Search a movie by name
# -----------------------------------
def search_movie(movie_name: str):
    url = f"{BASE_URL}/search/movie"

    params = {
        "api_key": TMDB_API_KEY,
        "query": movie_name
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()["results"]

    return []


# -----------------------------------
# Get movies by genre
# -----------------------------------
def get_movies_by_genre(genre: str, language: str = None):
    genre_id = GENRE_IDS.get(genre)

    if genre_id is None:
        return []

    url = f"{BASE_URL}/discover/movie"

    params = {
        "api_key": TMDB_API_KEY,
        "with_genres": genre_id,
        "with_original_language": language,
        "sort_by": "vote_average.desc",
        "vote_count.gte": 1000
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()["results"]

    return []