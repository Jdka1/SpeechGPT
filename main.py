# Loading environment variables
from dotenv import load_dotenv
import os

load_dotenv()
session_token = os.getenv('SESSION_TOKEN')

# -------------------------------------------------

from package.src import SpeechGPT

bot = SpeechGPT(session_token=session_token, voice_on=True)
response = bot.startListening()


# Return answer as well
# Package name to tts interface
# install all python packages it uses - requirements.txt


# git remote add origin https://github.com/Jdka1/SpeechGPT.git
# git branch -M main
# git push -u origin main
