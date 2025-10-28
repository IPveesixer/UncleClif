import os, requests, re, hashlib
from bs4 import BeautifulSoup

IMG_DIR = "assets"
os.makedirs(IMG_DIR, exist_ok=True)

PLACEHOLDER = os.path.join(IMG_DIR, "placeholder.jpg")

# create a tiny gray placeholder if not present
if not os.path.exists(PLACEHOLDER):
    from PIL import Image, ImageDraw, ImageFont
    img = Image.new("RGB", (1280, 720), color=(200,200,200))
    draw = ImageDraw.Draw(img)
    draw.text((40,340),"No image found",(50,50,50))
    img.save(PLACEHOLDER)

def get_image_for_url(url: str) -> str:
    try:
        html = requests.get(url, timeout=20).text
        soup = BeautifulSoup(html, "html.parser")
        og = soup.find("meta", property="og:image")
        if og and og.get("content"):
            img_url = og["content"]
        else:
            # fallback: first <img>
            img = soup.find("img")
            img_url = img["src"] if img and img.get("src") else None

        if not img_url:
            return PLACEHOLDER

        # Normalize protocol-less URLs
        if img_url.startswith("//"):
            img_url = "https:" + img_url

        # Download
        fname = hashlib.md5(img_url.encode()).hexdigest() + ".jpg"
        fp = os.path.join(IMG_DIR, fname)
        r = requests.get(img_url, timeout=30)
        if r.status_code == 200:
            with open(fp, "wb") as f:
                f.write(r.content)
            return fp
        return PLACEHOLDER
    except Exception:
        return PLACEHOLDER
