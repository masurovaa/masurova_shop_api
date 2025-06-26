from datetime import date
from rest_framework import serializers
from django.core.cache import cache

# from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from users.models import CustomUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserBaseSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length=150)
    birthday = serializers.DateField()
    password = serializers.CharField()


class AuthValidateSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class RegisterValidateSerializer(UserBaseSerializer):
    def validate_username(self, username):
        try:
            CustomUser.objects.get(username=username)
        except CustomUser.DoesNotExist :
            return username
        raise ValidationError("User уже существует!")

    def validate_email(self, email):
        try:
            CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            return email
        raise ValidationError("Email уже используется!")


class ConfirmationSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    code = serializers.CharField(max_length=6)

    def validate(self, attrs):
        user_id = attrs.get("user_id")
        code = attrs.get("confirmation_code")

        try:
            user = CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            raise ValidationError("User не существует!")
        
        cache_key = f'verify:{user.email}'
        stored_code = cache.get(cache_key)
        if stored_code != code:
            raise ValidationError("Неверный код подтверждения!")
        return attrs


class CustomToken(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        if not user.birthday:
            raise ValidationError("У пользователя не указана дата рождения.")
        today = date.today()
        age = (
            today.year
            - user.birthday.year
            - ((today.month, today.day) < (user.birthday.month, user.birthday.day))
        )

        if age < 18:
            raise ValidationError("Пользователю должно быть не менее 18 лет.")
        token = super().get_token(user)
        token["email"] = user.email
        token["username"] = user.username
        token["birthday"] = user.birthday.strftime("%Y-%m-%d")
        return token
