import streamlit as st
import sqlite3
import random
import os
import base64

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="PickFlick", page_icon="🎬", layout="wide")

# ---------- CSS ----------
st.markdown("""
<style>
            
.movie-card {
    background-color: #141414;
    border-radius: 12px;
    padding: 12px;
    text-align: center;
    transition: all 0.3s ease;
}
.movie-card:hover {
    transform: scale(1.05);
    box-shadow: 0 0 25px rgba(229, 9, 20, 0.8);
}
.movie-img {
    width: 140px;
    height: 210px;
    object-fit: cover;
    border-radius: 8px;
}
.movie-title {
    color: #E50914;
    font-weight: 600;
    margin-top: 8px;
    font-size: 0.95rem;
}
.movie-desc {
    color: #cccccc;
    font-size: 0.8rem;
}
.rating {
    color: #ffd700;
    font-weight: bold;
    font-size: 0.85rem;
}
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown("<h1 style='text-align:center;color:#E50914;'>PICKFLICK</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:gray;'>🎬 Find your next movie or get a random surprise!</p>", unsafe_allow_html=True)

# ---------- DATABASE ----------
conn = sqlite3.connect("movies.db", check_same_thread=False)
cursor = conn.cursor()

def fetch_movies():
    cursor.execute("SELECT * FROM movies")
    rows = cursor.fetchall()

    movies = []
    for row in rows:
        movies.append({
            "title": row[0],
            "genre": row[1].split(","),
            "image": row[2],
            "year": row[3],
            "rating": row[4],
            "desc": row[5]
        })
    return movies

movies = fetch_movies()

# ---------- SIDEBAR ----------
genres = sorted({g.strip() for movie in movies for g in movie["genre"]})
selected_genre = st.sidebar.multiselect("🎭 Select Genres", genres)

# ---------- SESSION STATE ----------
if "selected_movie" not in st.session_state:
    st.session_state.selected_movie = None

if "last_genre" not in st.session_state:
    st.session_state.last_genre = selected_genre

# Reset when genre changes
if st.session_state.last_genre != selected_genre:
    st.session_state.selected_movie = None
    st.session_state.last_genre = selected_genre

# ---------- SURPRISE BUTTON ----------
if st.sidebar.button("🎲 Surprise Me"):
    if selected_genre == "All":
        st.session_state.selected_movie = random.choice(movies)
    else:
        genre_movies = [m for m in movies if selected_genre in [g.strip() for g in m["genre"]]]
        if genre_movies:
            st.session_state.selected_movie = random.choice(genre_movies)

selected_movie = st.session_state.selected_movie

# ---------- IMAGE FUNCTION ----------
def get_image_base64(path):
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return None

# ---------- FILTER ----------
filtered_movies = []

for movie in movies:
    movie_genres = [g.strip() for g in movie["genre"]]

    # If no genre selected → show all
    if not selected_genre:
        filtered_movies.append(movie)

    # If any selected genre matches
    elif any(g in movie_genres for g in selected_genre):
        filtered_movies.append(movie)

# Apply surprise AFTER filtering
if selected_movie:
    filtered_movies = [selected_movie]

# ---------- DISPLAY ----------
if filtered_movies:
    for i in range(0, len(filtered_movies), 3):
        cols = st.columns(3)
        for j, movie in enumerate(filtered_movies[i:i+3]):   # ✅ FIXED BUG HERE
            with cols[j]:
                img_path = os.path.join("images", movie["image"])
                img_base64 = get_image_base64(img_path)

                if img_base64:
                    img_html = f"<img class='movie-img' src='data:image/jpeg;base64,{img_base64}'/>"
                else:
                    img_html = "<div style='color:white'>No Image</div>"

                st.markdown(f"""
                <div class="movie-card">
                    {img_html}
                    <div class="movie-title">{movie['title']} ({movie['year']})</div>
                    <div class="rating">⭐ {movie['rating']}</div>
                    <div class="movie-desc">{movie['desc']}</div>
                </div>
                """, unsafe_allow_html=True)
else:
    st.info("No movies found.")