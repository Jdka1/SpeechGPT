import sys, os

import speech_recognition
import pyttsx3

from .askgpt import askGPT
from .text_to_speech import tts


def blockPrint():
    sys.stdout = open(os.devnull, 'w')

def enablePrint():
    sys.stdout = sys.__stdout__


class SpeechGPT:
    def __init__(self, session_token, voice_on = True):
        self.session_token = session_token
        self.voice_on = voice_on
        self.recognizer = speech_recognition.Recognizer()
        self.voice = tts()
        

    def startListening(self):
        print("Listening...\n")
        while True:
            try:
                with speech_recognition.Microphone() as mic:
                    blockPrint()
                    self.recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                    audio = self.recognizer.listen(mic)
                    audio_text = self.recognizer.recognize_google(audio).lower()
                    enablePrint()
                    
                    if audio_text == "stop listening":
                        print("\nStopping listening.")
                        break
                    
                    print(f"Asking ChatGPT: {audio_text}")
                    answer = askGPT(message=audio_text, session_token=self.session_token)
                    answer = answer.replace('\n', ' ')
                    print(answer)

                    if self.voice_on:
                        self.voice.say(message=answer)
                    
                    return answer
                    
            except speech_recognition.UnknownValueError:
                self.recognizer = speech_recognition.Recognizer()
                continue

