import os
from atproto import Client
from dotenv import load_dotenv

def post(content):

    load_dotenv()

    api = Client()

    api.login(os.environ["BLUESKY_ACCOUNT"],os.environ["BLUESKY_PASS"])
    api.send_post(content)