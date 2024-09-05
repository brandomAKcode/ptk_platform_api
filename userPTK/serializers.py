from typing import Any, Dict, Optional, Type, TypeVar
from rest_framework import serializers
from .models import UserPTK
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.conf import settings as api_settings
from django.contrib.auth.models import update_last_login
from .models import UserPTK

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPTK
        fields = ['id', 'name', 'photo', 'zone', 'role']

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs: Dict[str, Any]) -> Dict[str, str]:
        data = super().validate(attrs)

        refresh = self.get_token(self.user)
        # get user to add aditional information
        user = UserPTK.objects.get(email=attrs['email'])
        data['token_refresh'] = str(refresh)
        data['token_access'] = str(refresh.access_token)
        data['user_id'] = user.id
        data['user_name'] = user.name
        data['user_role'] = user.role
        data['user_email'] = user.email

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return data