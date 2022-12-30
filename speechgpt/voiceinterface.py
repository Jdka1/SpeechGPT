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
    def __init__(self, session_token, wake_word = None, voice_on = True):
        self.session_token = session_token
        self.wake_word = wake_word
        self.voice_on = voice_on
        self.recognizer = speech_recognition.Recognizer()
        self.voice = tts()
        
        
    def listen(self, awake=False):
        if awake or self.wake_word is None:
            print('Listening...\n')
            
            with speech_recognition.Microphone() as mic:
                        blockPrint()
                        self.recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                        audio = self.recognizer.listen(mic)
                        audio_text = self.recognizer.recognize_google(audio).lower()
                        enablePrint()
            
            if audio_text == 'quit':
                print('Quitting.')
                return
                
            print(f"Asking ChatGPT: {audio_text}")
            answer = askGPT(message=audio_text, session_token=self.session_token)
            answer = answer.replace('\n', ' ')
            print(answer)
            
            if self.voice_on:
                self.voice.say(answer)
            
            return answer
            
                        
        else:
            while True:
                print("hi")
                try:
                    with speech_recognition.Microphone() as mic:
                        blockPrint()
                        self.recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                        audio = self.recognizer.listen(mic)
                        audio_text = self.recognizer.recognize_google(audio).lower()
                        enablePrint()
                        print(type(audio))
                    
                    
                    if audio_text == 'quit':
                        return    
                                
                    if audio_text == str(self.wake_word).lower():
                        print("Waking up...")
                        self.listen(awake=True)
                        return
                    
                        
                except speech_recognition.UnknownValueError:
                    self.recognizer = speech_recognition.Recognizer()
                    continue
            
        