from pyChatGPT import ChatGPT


def askGPT(message, session_token):
    api = ChatGPT(session_token)

    response = api.send_message(message)

    return response['message'].strip('\n')


