import textwrap, math, os

def seconds_to_ts(s):
    h = int(s // 3600); s -= h*3600
    m = int(s // 60); s -= m*60
    ss = int(s); ms = int((s-ss)*1000)
    return f"{h:02}:{m:02}:{ss:02},{ms:03}"

def text_to_srt(text: str, duration_s: float, wpm=150):
    # naive: split into ~10-second chunks based on words per minute
    words = text.split()
    words_per_sec = wpm/60.0
    approx_time = len(words)/words_per_sec
    total = max(duration_s, approx_time)
    chunks = []
    max_words_per_chunk = int(words_per_sec*10)  # ~10s
    for i in range(0, len(words), max_words_per_chunk):
        chunks.append(" ".join(words[i:i+max_words_per_chunk]))
    # write SRT
    srt_path = "overview.srt"
    start = 0.0
    step = total/len(chunks) if chunks else total
    with open(srt_path, "w") as f:
        for idx, chunk in enumerate(chunks, 1):
            end = min(total, start+step)
            f.write(f"{idx}\n{seconds_to_ts(start)} --> {seconds_to_ts(end)}\n{chunk}\n\n")
            start = end
    return srt_path
