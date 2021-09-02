from channels.generic.websocket import WebsocketConsumer
from django.contrib.auth.models import AnonymousUser

from .models import WebsocketClient


class NotificationsConsumer(WebsocketConsumer):
    def connect(self):
        # Get the user object
        user = self.scope['user']

        # Check if the user is an active user
        if user != AnonymousUser():
            # Accept the connection
            self.accept()

            # Make a database row with the channel name
            if hasattr(user, 'wsclient'):
                user.wsclient.delete()

            # Create the WebSocket client
            WebsocketClient.objects.create(channel_name=self.channel_name, user=user)
        else:
            # Reject the connection
            self.close()

    def disconnect(self, close_code):
        # Note that in some rare cases (power loss, etc) disconnect may fail
        # to run; this naive example would leave zombie channel names around.
        WebsocketClient.objects.filter(channel_name=self.channel_name).delete()

    def receive(self, text_data=None, bytes_data=None):
        # Get the user object
        user = self.scope['user']

        # Log the received message
        print(f"WebSocket Received Data: '{text_data}' from '{user}'")

    def notification_message(self, event):
        # Handles the "notification.message" event when it's sent to us.

        # Get the user object
        user = self.scope['user']

        # Log the message to send
        print(f"WebSocket Notification Message: '{event['text']}' to '{user}'")

        # Send the message over the WebSocket
        self.send(text_data=event['text'])
