import urllib.request
import urllib.parse
import json

movies = [
{"title":"Inception","year":2010},
{"title":"Parasite","year":2019},
{"title":"The Dark Knight","year":2008},
{"title":"Interstellar","year":2014},
{"title":"Joker","year":2019},
{"title":"Whiplash","year":2014},
{"title":"The Shawshank Redemption","year":1994},
{"title":"La La Land","year":2016},
{"title":"Fight Club","year":1999},
{"title":"The Godfather","year":1972},
{"title":"The Social Network","year":2010},
{"title":"Avengers: Endgame","year":2019},
{"title":"Get Out","year":2017},
{"title":"Coco","year":2017},
{"title":"Spirited Away","year":2001},
{"title":"The Grand Budapest Hotel","year":2014},
{"title":"Your Name","year":2016},
{"title":"The Prestige","year":2006},
{"title":"The Matrix","year":1999},
{"title":"Her","year":2013},
{"title":"Oppenheimer","year":2023},
{"title":"Little Women","year":2019},
{"title":"The Pianist","year":2002},
{"title":"The Imitation Game","year":2014},
{"title":"Black Swan","year":2010},
{"title":"Arrival","year":2016},
{"title":"Good Will Hunting","year":1997},
{"title":"Love, Rosie","year":2014},
{"title":"The Revenant","year":2015},
{"title":"The Wolf of Wall Street","year":2013},
{"title":"Dune","year":2021},
{"title":"Mamma Mia!","year":2008},
{"title":"Blade Runner 2049","year":2017},
{"title":"Mad Max: Fury Road","year":2015},
{"title":"The Green Mile","year":1999},
{"title":"Eternal Sunshine of the Spotless Mind","year":2004},
{"title":"The Truman Show","year":1998},
{"title":"Gone Girl","year":2014},
{"title":"The Shape of Water","year":2017},
{"title":"Hereditary","year":2018},
{"title":"Jojo Rabbit","year":2019},
{"title":"Once Upon a Time in Hollywood","year":2019},
{"title":"Inside Out","year":2015},
{"title":"Shutter Island","year":2010},
{"title":"Prisoners","year":2013},
{"title":"Knives Out","year":2019},
{"title":"Schindler's List","year":1993},
{"title":"The Sound of Music","year":1965},
{"title":"The Conjuring","year":2013}
]

urls = {}

for m in movies:
    title = m["title"]
    url = f"https://itunes.apple.com/search?term={urllib.parse.quote(title)}&entity=movie&limit=3"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=5) as response:
            data = json.loads(response.read().decode())
            results = data.get('results', [])
            if results:
                # get highest quality artwork
                img = results[0].get('artworkUrl100', '')
                img = img.replace('100x100bb', '600x600bb')
                urls[title] = img
                print(f"Found {title}: {img}")
            else:
                urls[title] = ""
                print(f"Not found {title}")
    except Exception as e:
        print(f"Error {title}: {e}")
        urls[title] = ""

with open("urls.json", "w") as f:
    json.dump(urls, f)
