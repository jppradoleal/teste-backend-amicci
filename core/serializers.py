from rest_framework import serializers
from rest_framework.exceptions import NotAuthenticated
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import LoginSerializer


class CustomRegisterSerializer(RegisterSerializer):
    username = None
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
        obj = super().create(validated_data)
        request = self.context.get("request")

        if not request and not hasattr(request, "user"):
            raise NotAuthenticated()

        obj.owner = request.user

        return obj
