def long_form_overview(text: str, title: str, published: str = "") -> str:
    """
    Heuristic summary for an "extended overview":
    - brief intro with title/date
    - key ideas (topical sentences)
    - implications / takeaways
    - closing CTA to read the full post
    """
    # Very simple heuristic "chunk and keep" approach to avoid heavy dependencies.
    # You can swap this for an LLM call (Gemini, etc.) if desired.
    words = text.split()
    if len(words) < 1200:
        body = text
    else:
        body = " ".join(words[:1200])  # cap around ~10 minutes of TTS

    intro = f"Extended overview of '{title}'. Published: {published or 'recently.'} "
    outro = f"\n\nFor the full context and all details, visit the original post."
    return intro + body + outro
