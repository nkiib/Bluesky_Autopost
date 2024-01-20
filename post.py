import os
from atproto import Client , models
from dotenv import load_dotenv

def post(Entry):

    load_dotenv()

    api = Client()

    embed_external = models.AppBskyEmbedExternal.Main(
        external = models.AppBskyEmbedExternal.External(
            title = Entry.title,
            description = Entry.summary,
            uri = Entry.entry_url
        )
    )

    api.login(os.environ["BLUESKY_ACCOUNT"],os.environ["BLUESKY_PASS"])
    api.send_post(Entry.__str__() , embed = embed_external)

