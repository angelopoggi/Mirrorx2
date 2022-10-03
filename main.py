#2022 Angelo Poggi
#angelo.poggi@enigmaconsulting.tech

import os

from src.mirror_speech import MirrorSpeech
from src.mirror_audio import MirrorAudio
from src.mirror_dream import MirrorDream


if __name__ == "__main__":
    record = MirrorAudio()
    speak = MirrorSpeech()
    dream = MirrorDream()
    record.mirror_record()
    speak.mirror_speech("recordedFile.wav")
    with open("prompt.txt", 'r') as prompt:
        input_prompt = prompt.readlines()
        print(input_prompt)
        dream.dream(input_prompt[0])

    os.system(f"fbi -a genearted_image.jpg")

