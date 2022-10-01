#Audio Class for Mirror Mirro Project

import pyaudio
import wave
import speech_recognition as sr

class MirrorAudio():
    def __init__(self):
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 44100
        self.CHUNK = 512
        self.RECORD_SECONDS = 5
        self.WAVE_OUTPUT_FILENAME = "recordedFile.wav"
        self.device_index = 2

    def mirror_record(self):
        audio = pyaudio.PyAudio()
        stream = audio.open(format=self.FORMAT, channels=self.CHANNELS,
                            rate=self.RATE, input=True, input_device_index=self.index,
                            frames_per_buffer=self.CHUNK)
        print("recording started")
        Recordframes = []

        for i in range(0, int(self.RATE / self.CHUNK * self.RECORD_SECONDS)):
            data = stream.read(self.CHUNK)
            Recordframes.append(data)
        print("recording stopped")

        stream.stop_stream()
        stream.close()
        audio.terminate()

        waveFile = wave.open(self.WAVE_OUTPUT_FILENAME, 'wb')
        waveFile.setnchannels(self.CHANNELS)
        waveFile.setsampwidth(audio.get_sample_size(self.FORMAT))
        waveFile.setframerate(self.RATE)
        waveFile.writeframes(b''.join(Recordframes))
        waveFile.close()

        r = sr.Recognizer()
        with sr.AudioFile(self.WAVE_OUTPUT_FILENAME) as source:
            # listen for the data (load audio to memory)
            audio_data = r.record(source)
            # recognize (convert from speech to text)
            text = r.recognize_google(audio_data)
            print(text)