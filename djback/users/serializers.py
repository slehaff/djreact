# users/serializers.py
from rest_framework import serializers
from . import models


class UserSerializer(serializers.ModelSerializer):
    "Docstring"
    class Meta:
        "Docstring"
        model = models.CustomUser
        fields = ('email', 'username', )
