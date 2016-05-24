import requests
import cred

URL = "https://graph.facebook.com/oauth/access_token"

def get_fb_access():
    r = requests.get(URL, {
        'client_id': cred.FB_APP_ID,
        'client_secret': cred.FB_SECRET ,
        'grant_type': 'client_credentials',
    })

    r.raise_for_status()
    key, value = r.text.split("=")
    assert key == "access_token"
    return value
