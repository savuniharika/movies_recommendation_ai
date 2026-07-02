from genre_agent import genre_graph
from rating_agent import rating_graph
from concurrent.futures import ThreadPoolExecutor

def run_parallel(state):

    with ThreadPoolExecutor() as executor:

        future1 = executor.submit(genre_graph.invoke, state)
        future2 = executor.submit(rating_graph.invoke, state)

        result1 = future1.result()
        result2 = future2.result()

    return {
        **result1,
        "top_rated_movies": result2["top_rated_movies"]
    }


state = {
    "user_query": "I want a romance movie",
    "genre": "",
    "genre_movies": [],
    "top_rated_movies": [],
    "similar_movies": [],
    "final_recommendations": []
}

result = run_parallel(state)

print(result)