from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework import serializers

from core.models import User, Place, Trip


class AuthUserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password',
        )

    def create(self, validated_data):
        if validated_data == "1":
            auth_user = User.objects.create_superuser(**validated_data)
        else:
            auth_user = User.objects.create_user(**validated_data)
        return auth_user


class AuthUserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=30)
    password = serializers.CharField(max_length=128, write_only=True)
    id = serializers.CharField(read_only=True)

    def create(self, validated_date):
        pass

    def update(self, instance, validated_data):
        pass

    def validate(self, data):
        username = data['username']
        password = data['password']
        user = authenticate(username=username, password=password)

        if user is None:
            raise serializers.ValidationError("Пользователя не существует")

        try:

            update_last_login(None, user)

            validation = {
                'username': user.username,
                'last_name': user.last_name,
                'first_name': user.first_name,
                'id': user.id,

            }
            return validation
        except Exception:
            raise serializers.ValidationError("Неверные данные для входа")


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ['name', 'descriptions', 'coordinate', 'photo']
        # exclude = ['photo',]


class TripSerializer(serializers.ModelSerializer):
    places = PlaceSerializer(many=True, read_only=True)

    class Meta:
        model = Trip
        fields = ['name', 'places', ]
