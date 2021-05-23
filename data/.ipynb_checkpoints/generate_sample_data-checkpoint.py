import dotenv
import os
import pandas as pd
import spotipy
import tidyspotify

from spotipy.oauth2 import SpotifyClientCredentials

dotenv.load_dotenv()

# Load env variables
config = {
    'client_id': os.environ["SPOTIPY_CLIENT_ID"],
    'client_secret': os.environ["SPOTIPY_CLIENT_SECRET"],
}
                                
sp = spotipy.Spotify(client_credentials_manager = SpotifyClientCredentials(**config))

# Define artists to select in sample data
select_artists = [
    "rihanna", "taylor swift", 
    "hamilton", "dear evan hansen", 
    "ed sheeran", "ariana grande",
    "bon jovi", "nirvana",
]


# Use API to grab that artist's audio features df
# Append together, export as csv
def append_and_export_csv(my_dict, file_name):
    df = pd.DataFrame()
    
    for key, value in my_dict.items():
        df = df.append(value)
        
    df.to_csv(f"./data/{file_name}", index=False)
    print("Exported to csv")


# Generate sample data
sample_dfs = {}
for i in select_artists:
    name = f"{i}.replace(' ', '_')"
    sample_dfs[name] = tidyspotify.get_artist_audio_features(i)

append_and_export_csv(sample_dfs, "artist_audio_features.csv") 


unique_artists = pd.read_csv("./data/artist_audio_features.csv")
unique_artists = unique_artists.artist_uri.drop_duplicates().to_list()

album_dfs = {}
for i in unique_artists:
    album_dfs[i] = tidyspotify.get_artist_albums(artist_id=i)
    
append_and_export_csv(album_dfs, "artist_albums.csv")