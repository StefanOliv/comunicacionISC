import json
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.db import database_sync_to_async

from asgiref.sync import sync_to_async

from django.contrib.auth.models import User

from .models import Canal_Comunicacion, Mensajes_canal, MensajePrivados

class ChatConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.modulo_comunicacion_name = self.scope['url_route']['kwargs']['canal_name']
        self.modulo_comunicacion_group_name = 'chat_%s' % self.modulo_comunicacion_name

        await self.channel_layer.group_add(
            self.modulo_comunicacion_group_name,
            self.channel_name
        )

        await self.accept()
            
    async def receive(self, text_data):
        data = json.loads(text_data)
        messege = data['messege']
        usernombre = data['usernombre']
        canal = data['canal']

        await self.salvar_mensaje(usernombre, canal, messege)

        await self.channel_layer.group_send(
            self.modulo_comunicacion_group_name,
            {
                'type': 'chat_message',
                'messege': messege,
                'usernombre': usernombre,
                'canal': canal,
            }
        )

    async def disconnect(self):
        await self.channel_layer.group_discard(
            self.modulo_comunicacion_group_name,
            self.channel_name 
        )

    async def chat_message(self, event):
        messege = event['messege']
        usernombre = event['usernombre']
        canal = event['canal']

        await self.send(text_data=json.dumps({
            'messege': messege,
            'usernombre': usernombre,
            'canal': canal,
        }))

    @sync_to_async
    def salvar_mensaje(self, username, canal, message):
        user = User.objects.get(username=username)
        canal = Canal_Comunicacion.objects.get(slug=canal)
        Mensajes_canal.objects.create(user=user, canal=canal, contenido=message)

# --------------------------------Consumer de mensajes privados------------------------------------------------

class PersonalConsumer(AsyncJsonWebsocketConsumer):
    # -----------------------Metodo para conectar con el web socket
    async def connect(self):
        my_id = self.scope['user'].id
        other_user_id = self.scope['url_route']['kwargs']['id']
        if int(my_id) > int(other_user_id):
            self.room_name = f'{my_id}-{other_user_id}'
        else:
            self.room_name = f'{other_user_id}-{my_id}'

        self.room_group_name = 'chat_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name,
        )

        await self.accept()
        # await self.send(text_data=self.room_group_name)
    # ------------------------Metodo para desconectar
    async def disconnect(self, code):
        self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_layer
        )
# ----------------Funcion que recibe el mensaje------------------------
    async def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data) 
        message = data['message']
        username = data['username']

        await self.save_message(username, self.room_group_name, message)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type':'chat_message',
                'message':message,
                'username':username,
            }
        )
    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        await self.send(text_data=json.dumps({
            'message':message,
            'username':username,
        }))
    @database_sync_to_async
    def save_message(self, username, thread_name, message):
        MensajePrivados.objects.create(sender = username, message=message, thread_name=thread_name)