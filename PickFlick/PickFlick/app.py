import streamlit as st
import random
import os

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="PickFlick", page_icon="🎬", layout="wide")

# ---------- CUSTOM CSS ----------
st.markdown("""
    <style>
    body {
        background-color: #000000;
        color: #ffffff;
        font-family: 'Helvetica Neue', sans-serif;
    }

    .title {
        font-size: 3rem;
        font-weight: 700;
        color: #E50914;
        text-align: center;
        margin-top: -20px;
        margin-bottom: 10px;
    }

    .subtitle {
        text-align: center;
        font-size: 1.1rem;
        color: #b3b3b3;
        margin-bottom: 40px;
    }

    .movie-card {
        background-color: #141414;
        border-radius: 12px;
        padding: 15px;
        text-align: center;
        transition: all 0.3s ease;
        box-shadow: 0 0 10px rgba(255, 0, 0, 0.2);
    }

    .movie-card:hover {
        transform: scale(1.05);
        box-shadow: 0 0 20px rgba(229, 9, 20, 0.7);
    }

    .movie-title {
        color: #E50914;
        font-size: 1.2rem;
        font-weight: 600;
        margin-top: 10px;
    }

    .movie-desc {
        color: #cccccc;
        font-size: 0.9rem;
        margin-top: 8px;
    }

    .rating {
        color: #ffd700;
        font-weight: bold;
        font-size: 0.95rem;
    }

    hr {
        border: 0;
        border-top: 1px solid #333;
        margin-top: 30px;
    }
    </style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown("<div class='title'>PICKFLICK</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>🎬 Find your next movie or get a random surprise!</div>", unsafe_allow_html=True)

# ---------- MOVIE DATA ----------
movies = [
{"title":"Inception","genre":["Sci-Fi","Thriller"],"image":"images/inception.jpg","year":2010,"rating":8.8,"desc":"A thief who enters people's dreams to steal secrets gets a final chance at redemption."},
{"title":"Parasite","genre":["Drama","Thriller"],"image":"images/parasite.jpg","year":2019,"rating":8.6,"desc":"A poor family schemes to infiltrate the lives of a wealthy household."},
{"title":"The Dark Knight","genre":["Action","Crime"],"image":"images/dark_knight.jpg","year":2008,"rating":9.0,"desc":"Batman faces chaos when the Joker wreaks havoc on Gotham City."},
{"title":"Interstellar","genre":["Sci-Fi","Adventure"],"image":"images/interstellar.jpg","year":2014,"rating":8.7,"desc":"Explorers travel through a wormhole to find a new home for humanity."},
{"title":"Joker","genre":["Drama","Crime"],"image":"images/joker.jpg","year":2019,"rating":8.4,"desc":"A failed comedian descends into madness, inspiring a violent revolution."},
{"title":"Whiplash","genre":["Drama","Music"],"image":"images/whiplash.jpg","year":2014,"rating":8.5,"desc":"A young drummer’s ambition collides with an abusive instructor’s perfectionism."},
{"title":"The Shawshank Redemption","genre":["Drama"],"image":"images/shawshank.jpg","year":1994,"rating":9.3,"desc":"Two imprisoned men form an enduring friendship over years of confinement."},
{"title":"La La Land","genre":["Romance","Music"],"image":"images/lalaland.jpg","year":2016,"rating":8.0,"desc":"A jazz musician and an aspiring actress chase dreams and love in LA."},
{"title":"Fight Club","genre":["Drama"],"image":"images/fightclub.jpg","year":1999,"rating":8.8,"desc":"An office worker and a soap maker form an underground fight club with dark consequences."},
{"title":"The Godfather","genre":["Crime","Drama"],"image":"images/godfather.jpg","year":1972,"rating":9.2,"desc":"An aging patriarch of a crime dynasty transfers control to his reluctant son."},
{"title":"The Social Network","genre":["Drama","Biography"],"image":"images/social_network.jpg","year":2010,"rating":7.7,"desc":"The story behind Facebook’s creation."},
{"title":"Avengers: Endgame","genre":["Action","Adventure"],"image":"images/endgame.jpg","year":2019,"rating":8.4,"desc":"The Avengers assemble to undo Thanos’ actions and restore balance."},
{"title":"Get Out","genre":["Horror","Thriller"],"image":"images/getout.jpg","year":2017,"rating":7.7,"desc":"A young African-American visits his white girlfriend’s family estate, uncovering disturbing secrets."},
{"title":"Coco","genre":["Animation","Family"],"image":"images/coco.jpg","year":2017,"rating":8.4,"desc":"A boy follows his passion for music in the Land of the Dead."},
{"title":"Spirited Away","genre":["Animation","Fantasy"],"image":"images/spirited_away.jpg","year":2001,"rating":8.6,"desc":"A girl enters a magical world of spirits while her parents are transformed into pigs."},
{"title":"The Grand Budapest Hotel","genre":["Comedy","Adventure"],"image":"images/grand_budapest.jpg","year":2014,"rating":8.1,"desc":"A concierge becomes entangled in a murder mystery in a fictional European hotel."},
{"title":"Your Name","genre":["Animation","Romance"],"image":"images/your_name.jpg","year":2016,"rating":8.4,"desc":"Two teenagers mysteriously swap bodies and seek to meet each other."},
{"title":"The Prestige","genre":["Mystery","Drama"],"image":"images/prestige.jpg","year":2006,"rating":8.5,"desc":"Two rival magicians compete for fame, secrets, and revenge."},
{"title":"The Matrix","genre":["Action","Sci-Fi"],"image":"images/matrix.jpg","year":1999,"rating":8.7,"desc":"A hacker discovers the reality he knows is a simulation and fights back."},
{"title":"Her","genre":["Romance","Sci-Fi"],"image":"images/her.jpg","year":2013,"rating":8.0,"desc":"A man falls in love with an AI operating system."},
{"title":"Oppenheimer","genre":["Drama","History"],"image":"images/oppenheimer.jpg","year":2023,"rating":8.6,"desc":"The story of the scientist behind the atomic bomb."},
{"title":"Little Women","genre":["Drama","Romance"],"image":"images/little_women.jpg","year":2019,"rating":7.8,"desc":"Four sisters navigate love, life, and ambition during the Civil War era."},
{"title":"The Pianist","genre":["Drama","History"],"image":"images/pianist.jpg","year":2002,"rating":8.5,"desc":"A Jewish pianist struggles to survive the Holocaust."},
{"title":"The Imitation Game","genre":["Biography","Drama"],"image":"images/imitation_game.jpg","year":2014,"rating":8.0,"desc":"A mathematician cracks Nazi codes during WWII."},
{"title":"Black Swan","genre":["Drama","Thriller"],"image":"images/black_swan.jpg","year":2010,"rating":8.0,"desc":"A ballerina loses herself in her role as the Swan Queen."},
{"title":"Arrival","genre":["Sci-Fi","Drama"],"image":"images/arrival.jpg","year":2016,"rating":7.9,"desc":"A linguist tries to communicate with alien visitors."},
{"title":"Good Will Hunting","genre":["Drama"],"image":"images/good_will_hunting.jpg","year":1997,"rating":8.3,"desc":"A janitor at MIT is a mathematical genius who needs help to find direction."},
{"title":"Love, Rosie","genre":["Romance","Comedy"],"image":"images/love_rosie.jpg","year":2014,"rating":7.2,"desc":"Two best friends face love and missed opportunities over the years."},
{"title":"The Revenant","genre":["Adventure","Drama"],"image":"images/revenant.jpg","year":2015,"rating":8.0,"desc":"A frontiersman seeks revenge after being left for dead."},
{"title":"The Wolf of Wall Street","genre":["Comedy","Biography"],"image":"images/wolf_wallstreet.jpg","year":2013,"rating":8.2,"desc":"The rise and fall of a stockbroker involved in corruption and fraud."},
{"title":"Dune","genre":["Sci-Fi","Adventure"],"image":"images/dune.jpg","year":2021,"rating":8.0,"desc":"The son of a noble family becomes embroiled in a battle for the desert planet Arrakis."},
{"title":"Mamma Mia!","genre":["Romance","Music","Comedy"],"image":"images/mamma_mia.jpg","year":2008,"rating":6.5,"desc":"A bride-to-be invites three men to her wedding, hoping to find her real father."},
{"title":"Blade Runner 2049","genre":["Sci-Fi","Mystery"],"image":"images/blade_runner.jpg","year":2017,"rating":8.0,"desc":"A new blade runner uncovers a secret that could reshape society."},
{"title":"Mad Max: Fury Road","genre":["Action","Adventure"],"image":"images/mad_max.jpg","year":2015,"rating":8.1,"desc":"In a post-apocalyptic world, Max helps a rebel to escape a tyrant."},
{"title":"The Green Mile","genre":["Drama","Fantasy"],"image":"images/green_mile.jpg","year":1999,"rating":8.6,"desc":"A death row guard discovers a prisoner has supernatural powers."},
{"title":"Eternal Sunshine of the Spotless Mind","genre":["Romance","Sci-Fi"],"image":"images/eternal_sunshine.jpg","year":2004,"rating":8.3,"desc":"A couple undergoes a procedure to erase memories of each other."},
{"title":"The Truman Show","genre":["Drama","Comedy"],"image":"images/truman_show.jpg","year":1998,"rating":8.1,"desc":"A man discovers his entire life is a TV show."},
{"title":"Gone Girl","genre":["Thriller","Mystery"],"image":"images/gone_girl.jpg","year":2014,"rating":8.1,"desc":"A husband becomes the prime suspect when his wife goes missing."},
{"title":"The Shape of Water","genre":["Romance","Fantasy"],"image":"images/shape_water.jpg","year":2017,"rating":7.3,"desc":"A mute woman forms a bond with a mysterious aquatic creature."},
{"title":"Hereditary","genre":["Horror","Drama"],"image":"images/hereditary.jpg","year":2018,"rating":7.3,"desc":"A family uncovers terrifying secrets after the death of their secretive grandmother."},
{"title":"Jojo Rabbit","genre":["War","History","Family","Comedy"],"image":"images/jojo_rabbit.jpg","year":2019,"rating":7.9,"desc":"A young boy in Nazi Germany has his worldview changed when he discovers his mother is hiding a Jewish girl."},
{"title":"Once Upon a Time in Hollywood","genre":["Comedy","Drama"],"image":"images/hollywood.jpg","year":2019,"rating":7.6,"desc":"An actor and his stunt double navigate 1969 Hollywood."},
{"title":"Inside Out","genre":["Animation","Family"],"image":"images/inside_out.jpg","year":2015,"rating":8.1,"desc":"Inside a young girl’s mind, emotions try to guide her through life."},
{"title":"Shutter Island","genre":["Thriller","Mystery"],"image":"images/shutter_island.jpg","year":2010,"rating":8.2,"desc":"A U.S. Marshal investigates a psychiatric facility on a remote island."},
{"title":"Prisoners","genre":["Thriller","Crime"],"image":"images/prisoners.jpg","year":2013,"rating":8.1,"desc":"A father takes matters into his own hands when his daughter disappears."},
{"title":"Knives Out","genre":["Mystery","Comedy"],"image":"images/knives_out.jpg","year":2019,"rating":7.9,"desc":"A detective investigates the death of a wealthy novelist."},
{"title":"Schindler's List","genre":["War","History","Biography","Drama"],"image":"images/schindlers_list.jpg","year":1993,"rating":9.0,"desc":"A German businessman saves over a thousand Jewish refugees during the Holocaust."},
{"title":"The Sound of Music","genre":["Music","Family","Drama"],"image":"images/sound_of_music.jpg","year":1965,"rating":8.0,"desc":"A governess brings joy and music to a strict family in Austria."},
{"title":"The Conjuring","genre":["Horror","Thriller"],"image":"images/conjuring.jpg","year":2013,"rating":7.5,"desc":"Paranormal investigators help a family terrorized by a dark presence in their farmhouse."},
]

# ---------- SIDEBAR ----------
genres = sorted({g for movie in movies for g in movie["genre"]})
selected_genre = st.sidebar.selectbox("🎭 Choose Genre", ["All"] + genres)

# Initialize session state for random movie
if "selected_movie" not in st.session_state:
    st.session_state.selected_movie = None

if st.sidebar.button("🎲 Surprise Me"):
    st.session_state.selected_movie = random.choice(movies)

selected_movie = st.session_state.selected_movie

# ---------- IMAGE PATH HELPER ----------
def get_image_path(filename):
    # FIX: The filename already contains "images/...", so we just join it with the current directory
    full_path = os.path.join(os.getcwd(), filename)
    if not os.path.exists(full_path):
        # Return a placeholder if the file is missing from the images folder
        return "https://via.placeholder.com/400x600.jpg?text=Image+Not+Found"
    return full_path

# ---------- FILTER MOVIES ----------
filtered_movies = []

for movie in movies:
    if selected_movie and movie != selected_movie:
        continue
    if selected_genre != "All" and selected_genre not in movie["genre"]:
        continue
    filtered_movies.append(movie)

# ---------- DISPLAY MOVIES ----------
if filtered_movies:
    for i in range(0, len(filtered_movies), 3):
        cols = st.columns(3)
        for j, movie in enumerate(filtered_movies[i:i+3]):
            if i + j < len(filtered_movies): # Prevents index error on the last row
                with cols[j]:
                    st.markdown("<div class='movie-card'>", unsafe_allow_html=True)
                    img_path = get_image_path(movie["image"])
                    # Use use_column_width instead of a fixed width for responsiveness
                    st.image(img_path, use_container_width="Default",width=200) 
                    st.markdown(f"<div class='movie-title'>{movie['title']} ({movie['year']})</div>", unsafe_allow_html=True)
                    st.markdown(f"<div class='rating'>⭐ {movie['rating']} | {' / '.join(movie['genre'])}</div>", unsafe_allow_html=True)
                    st.markdown(f"<div class='movie-desc'>{movie['desc']}</div>", unsafe_allow_html=True)
                    st.markdown("</div>", unsafe_allow_html=True)
        # Add some vertical space between rows
        st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)
else:
    st.info("No movies found for this genre.")