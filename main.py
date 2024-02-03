import feedparse
import post

def main():
    url = "https://nishikiout.net/feed"

    entries = feedparse.parse_feed(url)

    

    for entry in reversed(entries):
        post.post(entry)

    with open("latest_id.txt","w",encoding='utf-8') as f:
        f.write(entries[0].id)
    
    return 0

    

main()