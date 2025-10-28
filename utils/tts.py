from gtts import gTTS

def text_to_speech(text: str, out_mp3: str):
    tts = gTTS(text=text, lang="en")
    tts.save(out_mp3)
    return out_mp3
