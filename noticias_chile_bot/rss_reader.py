import feedparser

def get_chile_rss():
    feeds = [
        "https://www.emol.com/rss.asp",
        "https://www.cooperativa.cl/rss/",
        "https://www.latercera.com/rss/",
        "https://www.biobiochile.cl/noticias/rss/nacional.xml"
    ]
    items = []
    for url in feeds:
        d = feedparser.parse(url)
        for e in d.entries:
            img = e.get('media_content', [{'url':''}])[0]['url'] if 'media_content' in e else ''
            items.append({'title': e.title, 'link': e.link, 'published': e.get('published',''), 'image': img})
    return items