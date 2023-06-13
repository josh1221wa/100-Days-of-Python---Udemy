# Scrape Billboards Top 100 and Create a Spotify playlist with those.

import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import confidential
import pprint


date = input("Which year do you want to travel to? Type the date in the format YYYY-MM-DD: ")
year = date.split("-")[0]

url = f"https://www.billboard.com/charts/hot-100/{date}"

response = requests.get(url)
content = response.text

soup = BeautifulSoup(content, "html.parser")

titles = [tag.getText().strip("\n\t") for tag in soup.find_all(name="h3", id="title-of-a-story")][6::4][0:100]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://www.example.com",
        client_id=confidential.SPOTIFY_CLIENT_ID,
        client_secret=confidential.SPOTIFY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="./Day 46/token.txt"
    )
)
user_id = sp.current_user()["id"]

song_uris = []
for song in titles:
    track = sp.search(q=f"track: {song} year: {year}", type="track")
    try:
        uri = track["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} is not available on Spotify")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False, collaborative=False, description=f"The Billboard Top 100 on {date}")
playlist_uri = playlist["uri"]

sp.playlist_add_items(playlist_id=playlist_uri, items=song_uris)