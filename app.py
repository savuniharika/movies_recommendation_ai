import streamlit as st
from supervisor_graph import supervisor_graph

st.set_page_config(
    page_title="🎬 Movie Recommendation AI",
    page_icon="🎬",
    layout="centered"
)

st.title("🎬 Movie Recommendation AI")
st.write("Describe the movie you'd like to watch.")

# User input
query = st.text_input(
    "Movie Preference",
    placeholder="Example: I want a Telugu romance movie"
)

if st.button("Recommend Movies"):

    if query.strip() == "":
        st.warning("Please enter your movie preference.")
    else:
        state = {
            "user_query": query,
            "genre": "",
            "language": "",
            "genre_movies": [],
            "top_rated_movies": [],
            "similar_movies": [],
            "final_output": {}
        }

        result = supervisor_graph.invoke(state)

        output = result.get("final_output", {})

        st.success("Recommendations Generated!")

        st.subheader("Detected Genre")
        st.write(result.get("genre", "Not detected"))

        st.subheader("Language")
        st.write(output.get("language", "Unknown"))

        st.subheader("Top Recommended Movies")

        movies = result.get("top_rated_movies", [])

        if movies:
            for movie in movies:
                st.write(f"🎬 **{movie.get('title')}**")
        else:
            st.info("No movies found.")