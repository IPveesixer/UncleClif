import os, json, sys
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

def main():
    client_id = os.environ.get("YT_CLIENT_ID") or input("YT_CLIENT_ID: ").strip()
    client_secret = os.environ.get("YT_CLIENT_SECRET") or input("YT_CLIENT_SECRET: ").strip()
    client_config = {
        "installed": {
            "client_id": client_id,
            "client_secret": client_secret,
            "redirect_uris": ["http://localhost"],
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token"
        }
    }
    flow = InstalledAppFlow.from_client_config(client_config, SCOPES)
    creds = flow.run_local_server(port=0)
    print("\n=== SAVE THIS REFRESH TOKEN IN GITHUB SECRETS ===\n")
    print("YT_REFRESH_TOKEN:", creds.refresh_token)

if __name__ == "__main__":
    main()
