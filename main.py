#2022 Angelo Poggi
#angelo.poggi@enigmaconsulting.tech

from src.mirror_speech import MirrorSpeech
from src.mirror_audio import MirrorAudio

if __name__ == "__main__":
    record = MirrorAudio()
    speak = MirrorSpeech()
    record.mirror_record()
    speak.mirror_speech("recordedFile.wav")

