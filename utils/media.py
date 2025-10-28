import subprocess, json, os

def get_audio_duration(mp3_path: str) -> float:
    try:
        # ffprobe to get duration
        out = subprocess.check_output([
            "ffprobe", "-v", "error",
            "-show_entries", "format=duration",
            "-of", "default=noprint_wrappers=1:nokey=1",
            mp3_path
        ], stderr=subprocess.STDOUT).decode().strip()
        return float(out)
    except Exception:
        return 0.0

def image_and_audio_to_mp4(image_path: str, audio_path: str, out_mp4: str):
    # still image + audio → mp4
    cmd = [
        "ffmpeg", "-y",
        "-loop", "1",
        "-i", image_path,
        "-i", audio_path,
        "-c:v", "libx264", "-tune", "stillimage",
        "-c:a", "aac", "-b:a", "192k",
        "-shortest",
        "-pix_fmt", "yuv420p",
        out_mp4
    ]
    subprocess.check_call(cmd)
    return out_mp4
