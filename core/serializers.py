from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import LoginSerializer
from rest_framework.validators import UniqueValidator

from core.models import User


class CustomRegisterSerializer(RegisterSerializer):
    username = None
    email = serializers.EmailField(
        required=True, validators=[UniqueValidator(User.objects.all())]
    )
    password1 = serializers.CharField(write_only=True, style={"input_type": "password"})
    password2 = serializers.CharField(write_only=True, style={"input_type": "password"})

    def get_cleaned_data(self):
        super(CustomRegisterSerializer, self).get_cleaned_data()
        return {
            "password1": self.validated_data.get("password1", ""),
            "password2": self.validated_data.get("password2", ""),
            "email": self.validated_data.get("email", ""),
            "first_name": self.validated_data.get("first_name", ""),
            "last_name": self.validated_data.get("last_name", ""),
        }


class CustomLoginSerializer(LoginSerializer):
    username = None


class ModelSerializerWithOwner(serializers.ModelSerializer):
    def create(self, validated_data):
        validated_data["owner"] = self.context["request"].user
        return super().create(validated_data)
