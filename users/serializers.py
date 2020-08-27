from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed

from user_profile.models import UserProfile
from user_profile.serializers import UserProfileSerializer
from .models import User

class UserSerializer(serializers.ModelSerializer):
    # profile = UserProfileSerializer(many=False, read_only=True)
    class Meta:
        model = User
        fields = ['id','username', 'email','is_superuser','is_active']

class UserRegisterSerializer(serializers.ModelSerializer):
    # profile = UserProfileSerializer(required=False)
    password = serializers.CharField(max_length=100, min_length=5, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password']

    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username','')

        if not username.isalnum():
            raise serializers.ValidationError('The username should only contain alphanumeric characters')
        return attrs
    
    def create(self, validated_data):
        try:
            query = User.objects.get(is_superuser=True)
        except User.DoesNotExist:
            user = User.objects.create_superuser(**validated_data)
        else:
            user = User.objects.create_user(**validated_data)
            UserProfile.objects.create(
                user=user
            )
        print(UserProfile.objects.all())
        return user
        
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=100, min_length=5, write_only=True)
    username = serializers.CharField(max_length=255, read_only=True)
    tokens = serializers.CharField(read_only=True)

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        user = authenticate(email=email, password=password)
    
        if user is None:
            raise AuthenticationFailed('Invalid credential')
        if not user.is_verified:
            raise AuthenticationFailed('Please verify your email to login.')
        if user.is_activated is False:
            raise AuthenticationFailed('Account is not activated. Contact admin to activate your account.')

        return {
            'email': user.email,
            'username': user.username,
            'tokens': user.tokens,
        }
        return super().validate(attrs)