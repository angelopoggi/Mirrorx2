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
        print(input_prompt)
        input_prompt.append(prompt['medium'])
        input_prompt.append(prompt['artist'])
        input_prompt = f"{input_prompt[0]},{input_prompt[1]}, by {input_prompt[2]}"
        print(input_prompt)
        dream.dream(input_prompt)

    os.system(f"fbi -a {prompt}.jpg")

