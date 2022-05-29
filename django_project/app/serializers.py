from rest_framework import serializers
from django.contrib.auth.models import User


class UserModelSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        lower_email = value.lower()
        if User.filter(email__iexact=lower_email).exists():
            raise serializers.ValidationError("Email Already Exists")
        return lower_email

    class Meta:
        model = User
        fields = ["username", "password", "first_name", "last_name", "email"]