import trafilatura, requests
from readability import Document

def get_article_text(url: str) -> str:
    try:
        downloaded = trafilatura.fetch_url(url)
        if downloaded:
            txt = trafilatura.extract(downloaded, include_comments=False, include_tables=False)
            if txt and len(txt.split()) > 100:
                return txt
        # fallback to readability
        html = requests.get(url, timeout=20).text
        doc = Document(html)
        content = doc.summary(html_partial=True)
        text = trafilatura.extract(content, include_comments=False, include_tables=False)
        return text or ""
    except Exception:
        return ""
