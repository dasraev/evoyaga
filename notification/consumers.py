import json

from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync


# class NotificationConsumer(WebsocketConsumer):
#     def connect(self):
#         # self.room_name = 'notification'
#         self.room_group_name = 'notification_group'
#         async_to_sync(self.channel_layer.group_add) (
#             self.room_group_name,
#             self.channel_name
#         )

        
#         self.accept()
#         self.send(text_data=json.dumps({
#             'type': 'connection_established',
#             'message': 'You are now connected!',
#         }))

#     def disconnect(self, close_code):
#         # Leave room group
#         async_to_sync(self.channel_layer.group_discard)(
#             self.room_group_name,
#             self.channel_name
#         )

#     def send_notification(self, event):
#         self.send(text_data=json.dumps({
#             'type': 'notification_changed'
#         }))
    
#     def send_donation_notification(self, event):
#         self.send(text_data=json.dumps({
#             'type': 'donation_notification_changed'
#         }))
