from rest_framework import serializers

from models_module.models import User


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True, min_value=1)
    email = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    bio = serializers.CharField()
    birth_date = serializers.DateField()
    avatar = serializers.ImageField()
    auth_token = serializers.CharField()