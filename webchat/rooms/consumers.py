import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from django.contrib.auth.models import User
from .models import Room, Message

class Consumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name=self.scope['url_route']['kwargs']['room_name']
        self.room_group_name='chat_%s' % self.room_name
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
    
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data=json.loads(text_data)
        msg=data['message']
        username=data['username']
        room=data['room']
        if msg.isspace()==False and msg != "" : #On ne veut pas stocker ou envoyer les messages vides ou ne contenant que des espaces
            await self.storeMsg(msg,username,room)
            await self.channel_layer.group_send(
                self.room_group_name, {
                    'type': 'chatmsg',
                    'message': msg,
                    'username':username,
                    'room':room,
                }
            )

    async def chatmsg(self,event):
        msg=event['message']
        username=event['username']
        room=event['room']
        await self.send(text_data=json.dumps({
            'message': msg,
            'username':username,
            'room':room,
        }))
    
    @sync_to_async
    def storeMsg(self, msg, username, room):
        user=User.objects.get(username=username)
        room=Room.objects.get(slug=room)
        Message.objects.create(user=user,room=room,text=msg)
        