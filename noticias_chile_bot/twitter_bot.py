import os, tweepy

def connect_api():
    auth = tweepy.OAuth1UserHandler(
        os.getenv('TW_API_KEY'),
        os.getenv('TW_API_SECRET'),
        os.getenv('TW_ACCESS_TOKEN'),
        os.getenv('TW_ACCESS_SECRET')
    )
    return tweepy.API(auth)

def get_trending_hashtags(api, woeid=349859):  # WOEID Chile
    trends = api.trends_place(woeid)[0]['trends']
    tags = [t['name'] for t in trends if t['name'].startswith('#')]
    return tags[:5]

def post_tweet(api, text, image_path=None):
    if image_path:
        api.update_status_with_media(status=text, filename=image_path)
    else:
        api.update_status(text)