from channels.generic.websocket import AsyncWebsocketConsumer

counter = 0

class CounterConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add(
            "counter_group",
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            "counter_group",
            self.channel_name
        )

    async def receive(self, text_data):
        global counter
        counter += 1

        await self.channel_layer.group_send(
            "counter_group",
            {
                "type": "broadcast_count",
                "count": counter
            }
        )

    async def broadcast_count(self, event):
        await self.send(text_data=str(event["count"]))
