import os, time, json
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

def _creds():
    return Credentials(
        None,
        refresh_token=os.environ["YT_REFRESH_TOKEN"],
        client_id=os.environ["YT_CLIENT_ID"],
        client_secret=os.environ["YT_CLIENT_SECRET"],
        token_uri="https://oauth2.googleapis.com/token",
        scopes=SCOPES,
    )

def upload_video(mp4_path: str, title: str, description: str, tags=None, srt_path=None, privacy="public"):
    creds = _creds()
    yt = build("youtube", "v3", credentials=creds)
    body = {
        "snippet": {"title": title, "description": description, "tags": tags or []},
        "status": {"privacyStatus": privacy}
    }
    media = MediaFileUpload(mp4_path, mimetype="video/mp4", resumable=True)
    req = yt.videos().insert(part="snippet,status", body=body, media_body=media)
    resp = None
    while resp is None:
        status, resp = req.next_chunk()
        if status:
            print(f"Upload {int(status.progress() * 100)}%")
    vid = resp["id"]
    print("Uploaded video id:", vid)

    # Optional captions upload (basic SRT)
    if srt_path and os.path.exists(srt_path):
        captions_body = {"snippet": {"videoId": vid, "language": "en", "name": "Auto SRT"}}
        media = MediaFileUpload(srt_path, mimetype="application/octet-stream")
        yt.captions().insert(part="snippet", body=captions_body, media_body=media, sync=False).execute()
        print("Uploaded SRT captions.")
    return vid
