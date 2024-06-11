from rest_framework import serializers
from .models import Profile


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'username', 'email', 'phone_number', 'first_name', 'last_name', 'position', 'role']