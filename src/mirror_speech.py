import speech_recognition as sr

class MirrorSpeech():
    def __init__(self):
        pass
    
    def mirror_speech(self,filename):
        r = sr.Recognizer()
        with sr.AudioFile(filename) as source:
            # listen for the data (load audio to memory)
            audio_data = r.record(source)
            # recognize (convert from speech to text)
            text = r.recognize_google(audio_data)
            with open('prompt.txt', 'w') as prompt_file:
                prompt_file.write(text)

