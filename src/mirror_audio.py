#Audio Class for Mirror Mirro Project

import pyaudio
import wave

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
                            rate=self.RATE, input=True, input_device_index=self.device_index,
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


if __name__ == "__main__":
    foo = MirrorAudio()
    foo.mirror_record()