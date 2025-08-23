# notifications/serializers.py
from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    actor = serializers.ReadOnlyField(source='actor.username')
    target_type = serializers.SerializerMethodField()
    target_detail = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = ['id', 'recipient', 'actor', 'verb', 'target', 'timestamp', 'is_read', 'target_type', 'target_detail']
        read_only_fields = ['recipient', 'actor', 'verb', 'target', 'timestamp']

    def get_target_type(self, obj):
        return obj.content_type.model

    def get_target_detail(self, obj):
        if obj.target:
            if isinstance(obj.target, obj.target.__class__):
                return str(obj.target)
        return None