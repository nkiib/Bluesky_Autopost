import feedparser
from datetime import datetime, timedelta

class NH_entry:
    def __init__(self, title, entry_url, published, id, summary):
        self.title = title
        self.entry_url = entry_url
        self.published = published
        self.id = id
        self.summary = summary
        
    def __str__(self):
        return f"{self.title} - Nishiki-Hub"

def is_post(Entry):
    # エントリーの投稿時間を取得
    target_time = datetime.strptime(Entry.published, '%Y-%m-%dT%H:%M:%S%z')

    # 現在時刻を取得
    current_time = datetime.now(target_time.tzinfo)

    # 1日前の時間を計算
    one_day_ago = current_time - timedelta(days=1)

    with open("latest_id.txt","r",encoding='utf-8') as f:
        latest_id = f.read()
    
    if(latest_id == Entry.id):
        return False

    return target_time >= one_day_ago

def parse_feed(url):
    # RSSの取得と整形
    feed = feedparser.parse(url)

    # タイトルとURLを取得するためのリスト
    entries = []

    # 実際にフィードからタイトルとURLの取得
    for entry in feed.entries:
        entry_title = entry.get('title')
        entry_url = entry.get('link')
        entry_published = entry.get('published')
        entry_summary = entry.get('summary')
        entry_id = entry.get('id')

        Entry = NH_entry(entry_title , entry_url , entry_published , entry_id , entry_summary)

        if(is_post(Entry)):
            entries.append(Entry)
        else:
            break
        
    return entries
