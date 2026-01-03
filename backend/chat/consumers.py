from channels.generic.websocket import AsyncWebsocketConsumer

from channels.db import database_sync_to_async
from .models import Message

@database_sync_to_async
def save_message(user, content):
    return Message.objects.create(
        sender=user,
        content=content
    )


class GroupTestConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = "test_group"

        # Join group
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        await self.accept()
        print("✅ Connected and joined group")

    async def disconnect(self, close_code):
        # Leave group
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )
        print("❌ Disconnected and left group")

    async def receive(self, text_data):
        print("📨 Received:", text_data)

        # Broadcast to group
        await self.channel_layer.group_send(
            self.group_name,
            {
                "type": "broadcast_message",
                "message": text_data
            }
        )

    async def broadcast_message(self, event):
        # Send message to WebSocket
        await self.send(text_data=event["message"])
