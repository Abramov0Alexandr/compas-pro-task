from rest_framework import serializers

from user_selection.models import User


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        new_user = User.objects.create_user(**validated_data)
        return new_user


class UserRetrieveSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
