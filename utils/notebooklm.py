import os, json

# Placeholder thin wrapper to avoid hard-failing if you don't have access.
# If you do have NotebookLM Enterprise API access, implement the calls here.

def is_enabled():
    return bool(os.getenv("GCP_SA_KEY_JSON") and os.getenv("GOOGLE_PROJECT_ID"))

def ensure_notebook():
    # TODO: implement call to create or fetch notebook; return notebook id
    # For now, read NOTEBOOK_ID if present; else raise
    nb = os.getenv("NOTEBOOK_ID")
    if not nb:
        raise RuntimeError("NotebookLM not configured. Set NOTEBOOK_ID or implement creation.")
    return nb

def add_source(notebook_id: str, url: str, source_name: str):
    # TODO: call notebooks.sources.batchCreate with webContent
    print(f"[NotebookLM MOCK] add_source({notebook_id}, {url}, {source_name})")

def create_audio_overview(notebook_id: str, focus="Extended overview", language_code="en"):
    # TODO: call notebooks.audioOverviews.create
    print(f"[NotebookLM MOCK] create_audio_overview({notebook_id}, focus={focus})")
