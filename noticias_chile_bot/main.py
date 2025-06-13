import os, schedule, time
from rss_reader import get_chile_rss
from ai_summarizer import summarize_text
from image_fetcher import download_image
from twitter_bot import connect_api, get_trending_hashtags, post_tweet
from google_sheets import connect_sheet, exists_in_sheet, add_entry

sheet = connect_sheet()
api = connect_api()

def job():
    tags_viral = get_trending_hashtags(api)
    for e in get_chile_rss():
        if exists_in_sheet(sheet, e['link']): continue

        summary = summarize_text(e['title'])
        img = download_image(e['image'])
        local_tags = "#Chile #Noticias"
        hashtags = " ".join(tags_viral[:2] + [local_tags])
        tweet = f"{summary}\n\nLeer más: {e['link']}\n\n{hashtags}"

        post_tweet(api, tweet, img)
        add_entry(sheet, e['title'], summary, e['link'], e['published'], 'POSTED')
        print("Publicado:", e['title'])

schedule.every(15).minutes.do(job)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)