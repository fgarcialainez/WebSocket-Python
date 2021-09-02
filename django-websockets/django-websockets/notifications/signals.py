from django.db.models.signals import post_save
from channels.layers import get_channel_layer
from django.dispatch import receiver
from asgiref.sync import async_to_sync

from .models import Message


@receiver(post_save, sender=Message)
def create_message(sender, instance, created, **kwargs):
    if created:
        # Send the message over the WebSocket
        if hasattr(instance.user, 'wsclient'):
            # Get the associated WebSocket channel name
            channel_name = instance.user.wsclient.channel_name

            # Get the channel layer
            channel_layer = get_channel_layer()

            # Send the message to the consumer
            async_to_sync(channel_layer.send)(channel_name, {
                "type": "notification.message",
                "text": instance.text,
            })

            # Update the delivered flag
            instance.delivered = True
            instance.save()
