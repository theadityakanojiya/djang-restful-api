from rest_framework import serializers
from .models import SelfUser


class SelfUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SelfUser
        fields = '__all__'