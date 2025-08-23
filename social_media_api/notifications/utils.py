# notifications/utils.py
from django.contrib.contenttypes.models import ContentType
from .models import Notification

def create_notification(recipient, actor, verb, target):
    """
    Creates a notification for a given action.
    """
    content_type = ContentType.objects.get_for_model(target)
    Notification.objects.create(
        recipient=recipient,
        actor=actor,
        verb=verb,
        content_type=content_type,
        object_id=target.pk,
        target=target
    )