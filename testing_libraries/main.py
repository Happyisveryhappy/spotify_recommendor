from dotenv import load_dotenv
import requests
import os



load_dotenv()
clientID = os.getenv("CLIENT_ID")
clientSecret = os.getenv("CLIENT_SECRET")


def get_token():
    header = {"Content-Type" : "application/x-www-form-urlencoded"}
    client = f"grant_type=client_credentials&client_id={clientID}&client_secret={clientSecret}"

    req = requests.post('https://accounts.spotify.com/api/token', headers=header, data=client)
    response = req.json()
    accToken = response['access_token']
    return accToken


token = get_token()


def get_auth_header(token):
    return {'Authorization' : 'Bearer ' + token}


def get_arijit_top_tracks():
    reqURL = "https://api.spotify.com/v1/artists/4YRxDV8wJFPHPTeXepOstw/top-tracks" # arijit singh
    req = requests.get(reqURL , headers = get_auth_header)
    reqResult = req.json()
    return reqResult


arijit = get_arijit_top_tracks()
print(arijit)   
    