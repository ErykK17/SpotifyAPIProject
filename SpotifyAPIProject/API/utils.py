import base64
import json
import os

from dotenv import load_dotenv
from requests import post, get

load_dotenv()

client_id = os.getenv('CLIENTID')
client_secret = os.getenv('CLIENTSECRET')

def get_access_token(code, redirect_uri):

    spotify_url = 'https://accounts.spotify.com/api/token'

    body_params = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri' : redirect_uri
    }

    client_creds = f"{client_id}:{client_secret}"
    client_creds_b64 = base64.b64encode(client_creds.encode()).decode()

    headers = {
        'content_type': 'application/x-www-form-urlencoded',
        'Authorization': f'Basic {client_creds_b64}'
    }
    post_data = post(spotify_url, data=body_params, headers=headers)
    post_content = json.loads(post_data.content)
    auth_token = post_content['access_token']
    return auth_token


def get_top_items(type, access_token, time_range='medium_term', limit=50, offset=0):

    base_url = f'https://api.spotify.com/v1/me/top/{type}'

    query_params = {
        'time_range': time_range,
        'limit': limit,
        'offset': offset
    }

    query_string = '&'.join([f'{key}={value}' for key,value in query_params.items()])

    full_url = f'{base_url}?{query_string}'

    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    list = get(full_url, headers=headers)
    if list.status_code == 200:
        post_content = json.loads(list.content)
    else:
        print(f"Error: {list.status_code}")
    
    try:
        # Try to parse the JSON error message
        error_data = list.json()
        error_message = error_data.get('error', {}).get('message', 'No error message')
        print(f"Error Message: {error_message}")
    except ValueError:
        # If the response is not JSON, print the raw response text
        print("Could not parse error response. Raw response:")
        print(list.text)
    return post_content['items']