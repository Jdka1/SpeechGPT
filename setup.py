from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.1.0'
DESCRIPTION = "A voice interface for OpenAI's ChatGPT"

# Setting up
setup(
    name="speechgpt",
    version=VERSION,
    author="Jdka (Aryan Mehra)",
    author_email="staryan.mehra@gmail.com",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['pyChatGPT', 'pyttsx3', 'SpeechRecognition', 'pyaudio'],
    keywords=['python', 'ai', 'voice', 'text to speech'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ]
)