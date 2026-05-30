import lyricsgenius
from pathlib import Path
from slugify import slugify
import pandas as pd
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

genius = lyricsgenius.Genius(
    access_token = os.getenv("GENIUS_ACCESS_TOKEN"),
    skip_non_songs=True,
    remove_section_headers=False,
    timeout=10,
    retries=3
)

def get_lyrics(title, artist):
    try:
        print(f"Title: {title} ", f"Artist: {artist}")
        song = genius.search_song(title, artist)

        if song:
            return song.lyrics

    except Exception as e:
        print(f"Failed: {artist} - {title}: {e}")

    return None


OUTPUT_DIR = Path("S7code/sandbox/songs_corpus")
OUTPUT_DIR.mkdir(exist_ok=True)

def save_markdown(title, artist, lyrics):
    filename = OUTPUT_DIR / f"{slugify(artist)}-{slugify(title)}.md"

    content = f"""# {title}

**Artist:** {artist}

## Lyrics

{lyrics}
"""

    filename.write_text(content, encoding="utf-8")

def create_song_corpus():
    df = pd.read_csv("Songs_list.csv")
    for _, row in df.iterrows():
        title = row["Title"]
        artist = row["Artist"]
        lyrics = get_lyrics(title, artist)
        if lyrics:
            save_markdown(title, artist, lyrics)

if __name__ == "__main__":
    create_song_corpus()
    