from .models import UserManagement
from rest_framework import serializers

class UserManagementSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserManagement
        fields = ['id', 'username', 'email', 'mobile', 'created', 'modified']