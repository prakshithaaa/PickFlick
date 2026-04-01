import urllib.request
import urllib.parse
import json
import time

movies = [
"Inception", "Parasite (2019 film)", "The Dark Knight", "Interstellar (film)", "Joker (2019 film)"
]

for title in movies:
    url = f"https://en.wikipedia.org/w/api.php?action=query&prop=pageimages&format=json&piprop=original&titles={urllib.parse.quote(title)}"
    req = urllib.request.Request(url, headers={'User-Agent': 'PickFlick-Bot/1.0'})
    try:
        with urllib.request.urlopen(req, timeout=5) as response:
            data = json.loads(response.read().decode())
            pages = data['query']['pages']
            for page_id, page_info in pages.items():
                if 'original' in page_info:
                    print(f"{title}: {page_info['original']['source']}")
                else:
                    print(f"{title}: No image")
    except Exception as e:
        print(f"Error {title}: {e}")
    time.sleep(0.1)
