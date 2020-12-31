import requests
import config


def make_request(endpoint, params={}):
    params.update({"api-key": config.API_KEY})
    r = requests.get(config.API_URI + endpoint, params=params)
    if r.status_code != 200:
        raise Exception("API failure. Code: " + str(r.status_code))
    return r.json()


def get_tokens(user_id):
    data = make_request(f"/tokens/{user_id}/")
    return data["tokens"]


def subtract_tokens(user_id, tokens):
    data = make_request(f"/subtract/{user_id}/", params={"tokens": tokens})
    return data["success"]
