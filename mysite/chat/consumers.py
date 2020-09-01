# chat/consumers.py
import json,string
from channels.generic.websocket import AsyncWebsocketConsumer
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from random import Random
import random,base64,binascii
key=get_random_bytes(16)
iv=get_random_bytes(16)
#key=''.join(random.choices(string.ascii_uppercase+string.digits, k = 16)) 
#iv =''.join(random.choices(string.ascii_uppercase+string.digits, k = 16)) 

'''def pad(m):
    if(len(m)%2!=0):
        return m+b'\x00' '''
'''def rpad(m):
    n=b''
    print(len(m))
    for i in m:
        if(i=='\x00'):
            break
        else:
            print(i)
            n+=i
    return n'''

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        aes = AES.new(key, AES.MODE_CFB,iv)
        message=binascii.hexlify(aes.encrypt(message)).decode()
        print(message)
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        message=message.encode("ascii")
        aes = AES.new(key, AES.MODE_CFB,iv)
        message=aes.decrypt(binascii.unhexlify(message)).decode()
        
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))