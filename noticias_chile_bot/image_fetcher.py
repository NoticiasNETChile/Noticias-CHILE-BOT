import requests
from PIL import Image
from io import BytesIO

def download_image(url):
    if not url: return None
    try:
        resp = requests.get(url, timeout=10)
        img = Image.open(BytesIO(resp.content))
        path = 'temp.jpg'
        img.save(path)
        return path
    except:
        return None