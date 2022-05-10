import json
import pdb

from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from asgiref.sync import async_to_sync

from photo_backend_snp.settings import REDIS_INSTANCE


class WSConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        REDIS_INSTANCE.set(f"private_for_{self.scope['user'].id}", self.channel_name)
        await self.accept()

    async def disconnect(self, code):
        REDIS_INSTANCE.delete(f"private_for_{self.scope['user'].id}")

    async def liked_notification(self, event):
        await self.send(text_data=event["payload"])

    async def unliked_notification(self, event):
        await self.send(text_data=event["payload"])

    async def photo_approval_notification(self, event):
        await self.send(text_data=event["payload"])

    async def photo_deletion_notification(self, event):
        # NOT CREATED NEEDS TO WORK WITH STATES
        # DON'T FORGET
        await self.send(text_data=event["payload"])

    async def comment_notification(self, event):
        await self.send(text_data=event["payload"])
