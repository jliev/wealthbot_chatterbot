# chat/consumers.py
from channels.generic.websocket import WebsocketConsumer
import json

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

#       1.the connection has been built: Xinyu (finished)
#       2.get response from message to the user interface : Niu Hongqian and Liu xian
#       response = chatterbot.get_response(message)
#       3.update the user profile by the message: Li Jiahao
#       wealthbot_callback(message)

        response = message + "chatterbot not inplement yet"
        self.send(text_data=json.dumps({
            'message': response
        }))

def wealthbot_callback(message):
    pass