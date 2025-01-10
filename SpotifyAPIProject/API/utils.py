import base64
import json
import os

from dotenv import load_dotenv
from requests import post

load_dotenv()

client_id = os.getenv('CLIENTID')
clietn_secret = os.getenv('SECRETID')

def get_access_token(code, redirect_uri):

    spotify_url = 'https://accounts.spotify.com/api/token'

    body_params = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri' : redirect_uri
    }

    client_creds = f"{client_id}:{clietn_secret}"
    client_creds_b64 = base64.b64encode(client_creds.encode())

    headers = {
        'content_type': 'application/x-www-form-urlencoded',
        'Authorization': f'Basic {client_creds_b64}'
    }
    post_data = post(spotify_url, data=body_params, headers=headers)
    post_content = json.loads(post_data.content)
    auth_token = post_content['access_token']
    return auth_token
