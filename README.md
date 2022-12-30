# SpeechGPT

[![PyPi](https://img.shields.io/pypi/v/speechgpt.svg)](https://pypi.python.org/pypi/speechgpt)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A voice interface for OpenAI's ChatGPT

Credit to [@terry3041](https://github.com/terry3041) for [pyChatGPT](https://github.com/terry3041/pyChatGPT)

## Features

This package detects microphone input and coverts it to text using [Google's Speech Recognition API](https://cloud.google.com/speech-to-text). It then opens [ChatGPT](https://chat.openai.com/chat) and inputs the recognized text using selenium.

It can be used with a wake word, and it can also use text to speech to repeat ChatGPT's answer to the query. These arguements are specified in the creation of the class (see **Getting Started**)


## Getting Started

### Installation
```bash
pip3 install speechgpt
```

***or***

```bash
git clone https://github.com/Jdka1/SpeechGPT
```

Then navigate to ```SpeechGPT/speechgpt/``` and place the files in the same directory as your ```main.py``` file.


### Usage

#### Obtaining session_token

[Follow these steps](https://github.com/terry3041/pyChatGPT#usage) in [@terry3041's](https://github.com/terry3041) README.md

#### Importing as a module

```python
from speechgpt import SpeechGPT

session_token = "<__Secure-next-auth.session-token cookie from https://chat.openai.com/chat>"

bot = SpeechGPT(session_token=session_token) # Initializing the bot

bot.listen() # The bot will start listening and respond to whatever it is prompted with using ChatGPT
```
If the bot is initialized with a ```python
wake_word``` 

```python

```

```python
# .listen() only runs one cycle, so it needs to be put in a loop for it to answer more than one prompt

while True:
  bot.listen()
  
# If there is a wake_word set then the bot will wait until the phrase is spoken, then start listening
```



# wake word

# stop listening => quit

# returns answer

# need to install portaudio with homebrew pypi
