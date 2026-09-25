import requests as rq
from dotenv import load_dotenv
import os

load_dotenv()
clientID = os.getenv("CLIENT_ID")
clientSecret = os.getenv("CLIENT_SECRET")



# Getting access token
header = {"Content-Type" : "application/x-www-form-urlencoded"}
client = f"grant_type=client_credentials&client_id={clientID}&client_secret={clientSecret}"


req = rq.post('https://accounts.spotify.com/api/token', headers=header, data=client)
response = req.json()
print(response)


# Getting access to playlist
playlistLink = input('Enter playlist link: ')
id = playlistLink.split('/')[-1]
reqURL = f'https://api.spotify.com/v1/playlists/{id}/tracks'


playlistData = rq.get(reqURL, headers={"Authorization" : f"Bearer {accToken}"})
print(playlistData.json())