from tools import search_movie, get_movies_by_genre

print("----- Search Movie -----")

movies = search_movie("Interstellar")

for movie in movies[:5]:
    print(movie["title"])

print("\n----- Action Movies -----")

action_movies = get_movies_by_genre("Action")

for movie in action_movies[:5]:
    print(movie["title"])