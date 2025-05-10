from rest_framework import serializers
from .models import WalletUser, UserProfile
from django.contrib.auth.password_validation import validate_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = WalletUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'role', 'household']


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
            'phone_number', 'gender', 'date_of_birth',
            'address', 'currency', 'theme', 'likes', 'dislikes'
        ]


class UserRegistrationSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(required=False)
    password = serializers.CharField(write_only=True, validators=[validate_password])

    class Meta:
        model = WalletUser
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'role', 'household', 'profile']

    def create(self, validated_data):
        profile_data = validated_data.pop('profile', {})
        user = WalletUser.objects.create_user(**validated_data)

        # Fill in optional profile fields if provided
        for attr, value in profile_data.items():
            setattr(user.profile, attr, value)
        user.profile.save()

        return user
