from concurrent.futures import ThreadPoolExecutor
from genre_agent import genre_graph
from rating_agent import rating_graph

def run_async(state):

    with ThreadPoolExecutor() as executor:

        genre_task = executor.submit(genre_graph.invoke, state)
        rating_task = executor.submit(rating_graph.invoke, state)

        genre_result = genre_task.result()
        rating_result = rating_task.result()

    return {
        **genre_result,
        "top_rated_movies": rating_result.get("top_rated_movies", [])
    }


state = {
    "user_query": "I want a romance movie",
    "genre": "",
    "genre_movies": [],
    "top_rated_movies": [],
    "similar_movies": [],
    "final_recommendations": []
}

result = run_async(state)

print(result)