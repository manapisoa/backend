import json
from channels.generic.websocket import AsyncWebsocketConsumer
class NotifConsumers(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("notif_group",self.channel_name)
        print("connexion websoket etablis")
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("notif_group",self.channel_name)

    async def send_notif(self,event):
        await self.send(text_data= json.dumps(event["data"]))

    
    
