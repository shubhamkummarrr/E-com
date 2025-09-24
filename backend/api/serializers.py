from rest_framework import serializers
from .models import costumer
from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password

class CostumerSerializer(serializers.ModelSerializer):
    class Meta:
        model = costumer
        fields = '__all__'
        

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    # write_only so it never comes back in responses
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "first_name", "last_name"]

    def validate_password(self, value):
        # Uses Django’s built-in validators (length/complexity if configured)
        validate_password(value)
        return value

    def create(self, validated_data):
        # Properly hash the password
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class MeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "first_name", "last_name", "is_staff"]
        read_only_fields = fields
