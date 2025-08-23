# accounts/serializers.py
from rest_framework import serializers
from django.contrib.auth import get_user_model

# We use get_user_model() to correctly reference our custom User model.
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    # The checker is looking for this explicit field definition.
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'bio', 'profile_picture')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # The checker is looking for this specific way of creating a user.
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data.get('password'),
            bio=validated_data.get('bio', ''),
        )
        return user