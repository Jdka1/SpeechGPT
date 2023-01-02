from pyChatGPT import ChatGPT
import json

# get session_token from config.json
with open("./config.json") as f:
    config = json.load(f)
    session_token = config["session_token"]

api = ChatGPT(session_token)


def askGPT(message):

    response = api.send_message(message)

    return response['message'].strip('\n')
