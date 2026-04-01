import streamlit as st
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
    padding: 15px;
    text-align: center;
    transition: all 0.3s ease;
}

.movie-card:hover {
    transform: translateY(-10px);
    box-shadow: 0 0 30px red;
}

.movie-img {
    width: 180px;
    border-radius: 10px;
    transition: transform 0.3s ease;
}

.movie-card:hover .movie-img {
    transform: scale(1.1);
}

.movie-title {
    color: #E50914;
    font-weight: 600;
    margin-top: 10px;
}

.movie-desc {
    color: #cccccc;
    font-size: 0.9rem;
}

.rating {
    color: #ffd700;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown("<h1 style='text-align:center;color:#E50914;'>PICKFLICK</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:gray;'>🎬 Find your next movie or get a random surprise!</p>", unsafe_allow_html=True)

# ---------- MOVIES ----------
movies = [
{"title":"Inception","genre":["Sci-Fi","Thriller"],"image":"inception.jpg","year":2010,"rating":8.8,"desc":"A thief who enters people's dreams to steal secrets gets a final chance at redemption."},
{"title":"Parasite","genre":["Drama","Thriller"],"image":"parasite.jpg","year":2019,"rating":8.6,"desc":"A poor family schemes to infiltrate the lives of a wealthy household."},
{"title":"The Dark Knight","genre":["Action","Crime"],"image":"dark_knight.jpg","year":2008,"rating":9.0,"desc":"Batman faces chaos when the Joker wreaks havoc on Gotham City."},
{"title":"Interstellar","genre":["Sci-Fi","Adventure"],"image":"interstellar.jpg","year":2014,"rating":8.7,"desc":"Explorers travel through a wormhole to find a new home for humanity."},
{"title":"Joker","genre":["Drama","Crime"],"image":"joker.jpg","year":2019,"rating":8.4,"desc":"A failed comedian descends into madness, inspiring a violent revolution."},
{"title":"Whiplash","genre":["Drama","Music"],"image":"whiplash.jpg","year":2014,"rating":8.5,"desc":"A young drummer’s ambition collides with an abusive instructor’s perfectionism."},
{"title":"The Shawshank Redemption","genre":["Drama"],"image":"shawshank.jpg","year":1994,"rating":9.3,"desc":"Two imprisoned men form an enduring friendship over years of confinement."},
{"title":"La La Land","genre":["Romance","Music"],"image":"lalaland.jpg","year":2016,"rating":8.0,"desc":"A jazz musician and an aspiring actress chase dreams and love in LA."},
{"title":"Fight Club","genre":["Drama"],"image":"fightclub.jpg","year":1999,"rating":8.8,"desc":"An office worker and a soap maker form an underground fight club with dark consequences."},
{"title":"The Godfather","genre":["Crime","Drama"],"image":"godfather.jpg","year":1972,"rating":9.2,"desc":"An aging patriarch of a crime dynasty transfers control to his reluctant son."},
{"title":"The Social Network","genre":["Drama","Biography"],"image":"social_network.jpg","year":2010,"rating":7.7,"desc":"The story behind Facebook’s creation."},
{"title":"Avengers: Endgame","genre":["Action","Adventure"],"image":"endgame.jpg","year":2019,"rating":8.4,"desc":"The Avengers assemble to undo Thanos’ actions and restore balance."},
{"title":"Get Out","genre":["Horror","Thriller"],"image":"getout.jpg","year":2017,"rating":7.7,"desc":"A young African-American visits his white girlfriend’s family estate, uncovering disturbing secrets."},
{"title":"Coco","genre":["Animation","Family"],"image":"coco.jpg","year":2017,"rating":8.4,"desc":"A boy follows his passion for music in the Land of the Dead."},
{"title":"Spirited Away","genre":["Animation","Fantasy"],"image":"spirited_away.jpg","year":2001,"rating":8.6,"desc":"A girl enters a magical world of spirits while her parents are transformed into pigs."},
{"title":"The Grand Budapest Hotel","genre":["Comedy","Adventure"],"image":"grand_budapest.jpg","year":2014,"rating":8.1,"desc":"A concierge becomes entangled in a murder mystery in a fictional European hotel."},
{"title":"Your Name","genre":["Animation","Romance"],"image":"your_name.jpg","year":2016,"rating":8.4,"desc":"Two teenagers mysteriously swap bodies and seek to meet each other."},
{"title":"The Prestige","genre":["Mystery","Drama"],"image":"prestige.jpg","year":2006,"rating":8.5,"desc":"Two rival magicians compete for fame, secrets, and revenge."},
{"title":"The Matrix","genre":["Action","Sci-Fi"],"image":"matrix.jpg","year":1999,"rating":8.7,"desc":"A hacker discovers the reality he knows is a simulation and fights back."},
{"title":"Her","genre":["Romance","Sci-Fi"],"image":"her.jpg","year":2013,"rating":8.0,"desc":"A man falls in love with an AI operating system."},
{"title":"Oppenheimer","genre":["Drama","History"],"image":"oppenheimer.jpg","year":2023,"rating":8.6,"desc":"The story of the scientist behind the atomic bomb."},
{"title":"Little Women","genre":["Drama","Romance"],"image":"little_women.jpg","year":2019,"rating":7.8,"desc":"Four sisters navigate love, life, and ambition during the Civil War era."},
{"title":"The Pianist","genre":["Drama","History"],"image":"pianist.jpg","year":2002,"rating":8.5,"desc":"A Jewish pianist struggles to survive the Holocaust."},
{"title":"The Imitation Game","genre":["Biography","Drama"],"image":"imitation_game.jpg","year":2014,"rating":8.0,"desc":"A mathematician cracks Nazi codes during WWII."},
{"title":"Black Swan","genre":["Drama","Thriller"],"image":"black_swan.jpg","year":2010,"rating":8.0,"desc":"A ballerina loses herself in her role as the Swan Queen."},
{"title":"Arrival","genre":["Sci-Fi","Drama"],"image":"arrival.jpg","year":2016,"rating":7.9,"desc":"A linguist tries to communicate with alien visitors."},
{"title":"Good Will Hunting","genre":["Drama"],"image":"good_will_hunting.jpg","year":1997,"rating":8.3,"desc":"A janitor at MIT is a mathematical genius who needs help to find direction."},
{"title":"Love, Rosie","genre":["Romance","Comedy"],"image":"love_rosie.jpg","year":2014,"rating":7.2,"desc":"Two best friends face love and missed opportunities over the years."},
{"title":"The Revenant","genre":["Adventure","Drama"],"image":"revenant.jpg","year":2015,"rating":8.0,"desc":"A frontiersman seeks revenge after being left for dead."},
{"title":"The Wolf of Wall Street","genre":["Comedy","Biography"],"image":"wolf_wallstreet.jpg","year":2013,"rating":8.2,"desc":"The rise and fall of a stockbroker involved in corruption and fraud."},
{"title":"Dune","genre":["Sci-Fi","Adventure"],"image":"dune.jpg","year":2021,"rating":8.0,"desc":"The son of a noble family becomes embroiled in a battle for the desert planet Arrakis."},
{"title":"Mamma Mia!","genre":["Romance","Music","Comedy"],"image":"mamma_mia.jpg","year":2008,"rating":6.5,"desc":"A bride-to-be invites three men to her wedding, hoping to find her real father."},
{"title":"Blade Runner 2049","genre":["Sci-Fi","Mystery"],"image":"blade_runner.jpg","year":2017,"rating":8.0,"desc":"A new blade runner uncovers a secret that could reshape society."},
{"title":"Mad Max: Fury Road","genre":["Action","Adventure"],"image":"mad_max.jpg","year":2015,"rating":8.1,"desc":"In a post-apocalyptic world, Max helps a rebel to escape a tyrant."},
{"title":"The Green Mile","genre":["Drama","Fantasy"],"image":"green_mile.jpg","year":1999,"rating":8.6,"desc":"A death row guard discovers a prisoner has supernatural powers."},
{"title":"Eternal Sunshine of the Spotless Mind","genre":["Romance","Sci-Fi"],"image":"eternal_sunshine.jpg","year":2004,"rating":8.3,"desc":"A couple undergoes a procedure to erase memories of each other."},
{"title":"The Truman Show","genre":["Drama","Comedy"],"image":"truman_show.jpg","year":1998,"rating":8.1,"desc":"A man discovers his entire life is a TV show."},
{"title":"Gone Girl","genre":["Thriller","Mystery"],"image":"gone_girl.jpg","year":2014,"rating":8.1,"desc":"A husband becomes the prime suspect when his wife goes missing."},
{"title":"The Shape of Water","genre":["Romance","Fantasy"],"image":"shape_water.jpg","year":2017,"rating":7.3,"desc":"A mute woman forms a bond with a mysterious aquatic creature."},
{"title":"Hereditary","genre":["Horror","Drama"],"image":"hereditary.jpg","year":2018,"rating":7.3,"desc":"A family uncovers terrifying secrets after the death of their secretive grandmother."},
{"title":"Jojo Rabbit","genre":["War","History","Family","Comedy"],"image":"jojo_rabbit.jpg","year":2019,"rating":7.9,"desc":"A young boy in Nazi Germany has his worldview changed when he discovers his mother is hiding a Jewish girl."},
{"title":"Once Upon a Time in Hollywood","genre":["Comedy","Drama"],"image":"hollywood.jpg","year":2019,"rating":7.6,"desc":"An actor and his stunt double navigate 1969 Hollywood."},
{"title":"Inside Out","genre":["Animation","Family"],"image":"inside_out.jpg","year":2015,"rating":8.1,"desc":"Inside a young girl’s mind, emotions try to guide her through life."},
{"title":"Shutter Island","genre":["Thriller","Mystery"],"image":"shutter_island.jpg","year":2010,"rating":8.2,"desc":"A U.S. Marshal investigates a psychiatric facility on a remote island."},
{"title":"Prisoners","genre":["Thriller","Crime"],"image":"prisoners.jpg","year":2013,"rating":8.1,"desc":"A father takes matters into his own hands when his daughter disappears."},
{"title":"Knives Out","genre":["Mystery","Comedy"],"image":"knives_out.jpg","year":2019,"rating":7.9,"desc":"A detective investigates the death of a wealthy novelist."},
{"title":"Schindler's List","genre":["War","History","Biography","Drama"],"image":"schindlers_list.jpg","year":1993,"rating":9.0,"desc":"A German businessman saves over a thousand Jewish refugees during the Holocaust."},
{"title":"The Sound of Music","genre":["Music","Family","Drama"],"image":"sound_of_music.jpg","year":1965,"rating":8.0,"desc":"A governess brings joy and music to a strict family in Austria."},
{"title":"The Conjuring","genre":["Horror","Thriller"],"image":"conjuring.jpg","year":2013,"rating":7.5,"desc":"Paranormal investigators help a family terrorized by a dark presence in their farmhouse."},
{"title": "Hacksaw Ridge","genre": ["War", "Drama", "Biography", "History"],"image": "hacksaw_ridge.jpg","year": 2016,"rating": 8.1,"desc": "A WWII medic serves without carrying a weapon."},
{"title":"Maleficent","genre":["Fantasy","Adventure","Family","Action"],"image":"maleficent.jpg","year":2014,"rating":7.0,"desc":"The untold story of a powerful fairy whose betrayal leads her down a dark path."}
]

# ---------- SIDEBAR ----------
genres = sorted({g for movie in movies for g in movie["genre"]})
selected_genre = st.sidebar.selectbox("🎭 Genre", ["All"] + genres)

if "selected_movie" not in st.session_state:
    st.session_state.selected_movie = None

# Reset when genre changes
if "last_genre" not in st.session_state:
    st.session_state.last_genre = selected_genre

if st.session_state.last_genre != selected_genre:
    st.session_state.selected_movie = None
    st.session_state.last_genre = selected_genre

# 🎲 Surprise button (FIXED)
if st.sidebar.button("🎲 Surprise Me"):
    if selected_genre == "All":
        st.session_state.selected_movie = random.choice(movies)
    else:
        genre_movies = [m for m in movies if selected_genre in m["genre"]]
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
    if selected_genre != "All" and selected_genre not in movie["genre"]:
        continue
    filtered_movies.append(movie)

# Apply surprise AFTER filtering
if selected_movie:
    filtered_movies = [selected_movie]

# ---------- DISPLAY ----------
if filtered_movies:
    for i in range(0, len(filtered_movies), 3):
        cols = st.columns(3)
        for j, movie in enumerate(filtered_movies[i:i+3]):
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