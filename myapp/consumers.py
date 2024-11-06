# myapp/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer


class DataConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("data_updates", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("data_updates", self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        # Here you could process incoming data if needed
        await self.channel_layer.group_send(
            "data_updates",
            {
                "type": "send_data",
                "data": data
            }
        )

    async def send_data(self, event):
        data = event["data"]
        await self.send(text_data=json.dumps(data))