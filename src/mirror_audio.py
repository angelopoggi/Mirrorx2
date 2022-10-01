#Audio Class for Mirror Mirro Project

import logging
from datetime import datetime
from pytz import timezone
import wave

import pyaudio

class MirrorAudio():
    def __init__(self):
        self.CHUNK = 1024
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 2
        self.RATE = 44100
        self.RECORD_SECONDS = 5
        self.WAVE_OUTPUT_FILENAME = "output.wav"
        self.pyaudio = pyaudio.PyAudio()
        self.TZ = "EST"

    def mirror_record(self):
        tz = timezone(self.TZ)
        frames = []
        stream = self.pyaudio(
            format=self.FORMAT,
            channels=self.CHANNELS,
            rate=self.RATE,
            input=True,
            frames_per_buffer=self.CHUNK
        )
        logging.log(f"Started Recording at {datetime.now(tz)}")
        for i in range(0, int(self.RATE / self.CHUNK * self.RECORD_SECONDS)):
            data = stream.read(self.CHUNK)
            frames.append(data)

        stream.stop_stream()
        stream.close()
        self.pyaudio.terminate()

        wf = wave.open(self.WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(self.pyaudio.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(b''.join(frames))
        wf.close()

if __name__ == "__main__":
    audio = MirrorAudio()
    audio.mirror_record()