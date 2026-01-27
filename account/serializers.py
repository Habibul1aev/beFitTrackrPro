import uuid

from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from account.models import User
from django.contrib.auth.password_validation import validate_password



class AccountUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'avatar', 'gender', 'age', 'growth', 'goal', 'physical_activity', 'weight_value',
                  'first_name', 'last_name', 'email', 'phone_number')

class LoginSerializer(serializers.Serializer):

    email = serializers.EmailField()
    password = serializers.CharField()


class RegisterSerializers(serializers.ModelSerializer):

    password1 = serializers.CharField(validators=[validate_password], max_length=128)
    password2 = serializers.CharField(max_length=128)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'password1', 'password2')


    def validate(self, attrs):
        password1 = attrs.get('password1')
        password2 = attrs.get('password2')

        if password2 != password1:
            raise serializers.ValidationError({'password2': ['Пароль не совподает']})

        return attrs

    def create(self, validated_data):
        password = validated_data.pop('password1')
        validated_data.pop('password2')
        validated_data['password'] = make_password(password)
        validated_data['username'] = f'user_{uuid.uuid4().hex[:6]}'
        validated_data['avatar'] = '/avatars/stiker2.webp'

        return super().create(validated_data)