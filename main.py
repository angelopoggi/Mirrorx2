#2022 Angelo Poggi
#angelo.poggi@enigmaconsulting.tech

import os

from src.mirror_speech import MirrorSpeech
from src.mirror_audio import MirrorAudio
from src.mirror_dream import MirrorDream
from utils.rand_util import RandUtils

if __name__ == "__main__":
    record = MirrorAudio()
    speak = MirrorSpeech()
    dream = MirrorDream()
    record.mirror_record()
    rand = RandUtils()
    prompt = rand.rand_prompt()
    print(prompt)
    speak.mirror_speech("recordedFile.wav")
    with open("prompt.txt", 'r') as prompt:
        input_prompt = prompt.readlines()
        input_prompt = f"{input_prompt}, {prompt['medium']}, by {prompt['artist']}"
        dream.dream(input_prompt)

    os.system(f"fbi -a {prompt}.jpg")

