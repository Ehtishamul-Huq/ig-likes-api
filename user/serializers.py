from rest_framework import serializers
from user.models import User, UserProfile
import uuid
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework_jwt.settings import api_settings

from rest_framework_simplejwt.tokens import RefreshToken

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'instagram_id')

class UserRegistrationSerializer(serializers.ModelSerializer):

        profile = UserSerializer(required=False)

        class Meta:
            model = User
            fields = ('id', 'email', 'password', 'profile')
            extra_kwargs = {'password':{'write_only':True}}

        def create(self, validated_data):
            profile_data = validated_data.pop('profile')
            user = User.objects.create_user(**validated_data)
            UserProfile.objects.create(
                user = user,
                first_name = profile_data['first_name'],
                last_name = profile_data['last_name'],
                instagram_id = profile_data['instagram_id']
            )
            return user

class UserLoginSerializer(serializers.Serializer):

    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)
    id = serializers.UUIDField(required=False)

    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password", None)
        user = authenticate(email=email, password=password)
        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password is not found.'
            )
        try:
            jwt_token = RefreshToken.for_user(user
            )
            update_last_login(None, user)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                'User with given email and password does not exists'
            )
        return {
            'email':user.email,
            'token': jwt_token.access_token
        }