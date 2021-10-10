import json

from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth import get_user_model

from ..models import Stream, Streamer, Message

User = get_user_model()


class MsgConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print(f'connect {self.scope["user"]}')
        print(f"id = {self.scope['url_route']['kwargs']['id']}")

        self.room_group_name = f"{self.scope['url_route']['kwargs']['id']}"

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

        test = json.dumps({'test': 'OwO it`s alive'})
        await self.send(test)

    async def disconnect(self, code):
        print('disconnect')

        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

        return await super().disconnect(code)

    async def receive(self, text_data=None, bytes_data=None):
        print('receive')
        print(text_data)

        data = json.loads(text_data)
        user = self.scope["user"]

        message = await self.save_message(user, data)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'name': f'{self.scope["user"]}',
                'message': data['text'],
                'datetime': f'{message.datetime}',
            }
        )

        return await super().receive(text_data=text_data, bytes_data=bytes_data)

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            'name': event['name'],
            'message': event['message'],
            'datetime': event['datetime'],
        }))

    @sync_to_async
    def save_message(self, user, data):
        stream = Stream.objects.filter(id=data["id"]).first()
        streamer = Streamer.objects.filter(stream=stream, user=user).first()

        return Message.objects.create(
            stream=stream,
            streamer=streamer,
            text=data['text'],
        )
