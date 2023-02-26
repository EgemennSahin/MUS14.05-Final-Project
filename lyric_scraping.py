import lyricsgenius
from dotenv import load_dotenv
import os

# Load the .env file for the Genius API token
load_dotenv()
token = os.getenv('GENIUS_ACCESS_TOKEN')

# Create a Genius object
genius = lyricsgenius.Genius(token, timeout=15, retries=3)

# List of influences to search for
influences = ["Drake", "Kanye West"]

# Get each artist's top 50 songs' lyrics
for artist in influences:
    songs: dict = genius.search_artist(artist)

    song_lyrics = songs.to_text(filename=artist + "_lyrics.txt",)
