# SpeechGPT

[![PyPi](https://img.shields.io/pypi/v/speechgpt.svg)](https://pypi.python.org/pypi/speechgpt)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A voice interface for OpenAI's ChatGPT 🎙

Credit to [@terry3041](https://github.com/terry3041) for [pyChatGPT](https://github.com/terry3041/pyChatGPT) ❤️

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

It is not uncommon that there are errors when installing pyaudio. If you are on macOS you may have to use homebrew to install ```portaudio```.

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
If the bot is initialized with a ```wake_word``` value then it will wait until it hears that phrase when ```bot.listen()``` is called, and then it will start listening.

If the bot is initialized with ```voice_on = True``` as an arguement, then it will use text to speech to play back ChatGPT's response.

```python
# How to initialize SpeechGPT with wake_word and voice_on
bot = SpeechGPT(session_token=session_token,
                wake_word="wake up",
                voice_on=True)
```

```.listen()``` only runs one cycle, so it needs to be put in a loop for it to answer more than one prompt

```python
while True:
  bot.listen()
```

If the bot hears ***"quit"*** at any stage after ```.listen()``` is called then it will quit.


## Disclaimer

This package is not affiliated with OpenAI in any way. Use at your own risk. I am not responsible for any damage or harm caused by this project. Please read [OpenAI's Terms of Service](https://beta.openai.com/terms) before using this module.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
