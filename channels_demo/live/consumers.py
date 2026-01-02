from channels.generic.websocket import AsyncWebsocketConsumer

counter = 0

class CounterConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def receive(self, text_data):
        global counter
        if text_data == "increment":
            counter += 1
            await self.send(text_data=str(counter))
