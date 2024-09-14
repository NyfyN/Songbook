from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'e_mail', 'password', 'confirm_password']

    def validate(self, data):
        # Walidacja, aby upewnić się, że hasła się zgadzają
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError(
                {"non_field_errors": ["Passwords do not match"]})
        return data

    def create(self, validated_data):
        # Usuwamy confirm_password, aby nie był zapisany w bazie danych
        validated_data.pop('confirm_password')
        # Haszowanie hasła
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)
