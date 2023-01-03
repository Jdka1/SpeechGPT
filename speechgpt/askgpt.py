from pyChatGPT import ChatGPT


class ChatGPTAPI:
    def __init__(self, session_token):
        self.session_token = session_token
        self.api = ChatGPT(session_token)
        
    def askGPT(self, message, session_token):
        response = self.api.send_message(message)
        return response['message'].strip('\n')


