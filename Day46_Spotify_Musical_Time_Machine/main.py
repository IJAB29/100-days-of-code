import requests
import lxml
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
import pprint
import time

URL = "https://www.billboard.com/charts/hot-100/"

# date = input("Which year would you like to travel to?(YYYY-MM-DD) ")
date = '2012-12-31'

contents = requests.get(f"{URL}{date}", timeout=60).text
soup = BeautifulSoup(contents, "lxml")

top_songs = soup.select(selector="li #title-of-a-story")
top_songs_artists = soup.select(selector="li ul li span")
song_artists = []
for artist in top_songs_artists:
    name = artist.getText().strip()
    try:
        int(name)
    except ValueError:
        if len(name) > 1:
            song_artists.append(name)
song_titles = [song.getText().strip() for song in top_songs]

auth_manager = SpotifyOAuth(client_id=os.environ.get("SPOTIPY_CLIENT_ID"),
                            client_secret=os.environ.get("SPOTIPY_CLIENT_SECRET"),
                            redirect_uri="http://example.com",
                            scope="playlist-modify-private",
                            show_dialog=True,
                            cache_path="token.txt")
sp = spotipy.Spotify(auth_manager=auth_manager)
user_id = sp.current_user()["id"]


def createPlaylist(song_titles, song_artists, date, user_id):
    song_uris = []
    year = int(date.split('-')[0])
    for index in range(0, len(song_titles)):
        song_details = sp.search(f"track:{song_titles[index].lower()} artist:{song_artists[index].lower()}"
                                 f" year:{year - 5}-{year}", type="track")
        try:
            song_uri = song_details["tracks"]["items"][0]["uri"]
            song_uris.append(song_uri)
        except IndexError:
            pass
    playlist = sp.user_playlist_create(user=user_id,
                                       name=f"{date} Billboard 100",
                                       public=False,
                                       description=f"Top 100 songs from the date {date}")
    sp.playlist_add_items(playlist_id=playlist["id"],
                          items=song_uris)


stop = False
while not stop:
    try:
        createPlaylist(song_titles, song_artists, date, user_id)
    except requests.exceptions.ReadTimeout:
        print("Exception")
        time.sleep(5)
    else:
        stop = True
