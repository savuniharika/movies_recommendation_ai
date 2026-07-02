from supervisor_graph import supervisor_graph

state = {
    "user_query": "I want a telugu romance movie",
    "genre": "",
    "language": "",
    "genre_movies": [],
    "top_rated_movies": [],
    "similar_movies": [],
    "final_output": {}
}

result = supervisor_graph.invoke(state)

# SAFE CHECK
output = result.get("final_output", {})

print("\n🎬 MOVIE RECOMMENDATIONS\n")

print("Genre:", result.get("genre"))
print("Language:", output.get("language"))

print("\nTop Movies:")
for movie in result.get("top_rated_movies", []):
    print("-", movie.get("title"))