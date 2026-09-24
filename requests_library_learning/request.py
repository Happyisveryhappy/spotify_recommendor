from tokenize import String

import requests as rq

# Getting access token
header = {"Content-Type" : "application/x-www-form-urlencoded"}
client = f"grant_type=client_credentials&client_id=yourclientID&client_secret=yourclientsecret"


req = rq.post('https://accounts.spotify.com/api/token', headers=header, data=client)
response = req.json()
accToken = response['access_token']
print(accToken)


# Getting access to playlist
playlistLink = input('Enter playlist link: ')
id = playlistLink.split('/')[-1]
reqURL = f'https://api.spotify.com/v1/playlists/{id}/items'


playlistData = rq.get(reqURL, headers={"Authorization" : f"Bearer {accToken}"})
print(playlistData.json())