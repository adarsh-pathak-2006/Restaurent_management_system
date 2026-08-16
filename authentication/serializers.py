from rest_framework.serializers import ModelSerializer
from .models import User

class UserGetSerializer(ModelSerializer):
    class Meta:
        model=User
        fields=['username', 'email', 'role']

class RegisterSerializer(ModelSerializer):
    class Meta:
        model=User
        fields=['username', 'email', 'password', 'role']