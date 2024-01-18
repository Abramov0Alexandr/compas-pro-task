from rest_framework import serializers

from user_selection.models import User


class CreateUserSerializer(serializers.ModelSerializer):
    """
    Serializer class for creating a new user, used in UserCreateAPIView.
    The entered user password will be hashed.
    """

    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        new_user = User.objects.create_user(**validated_data)
        return new_user


class UserRetrieveSerializers(serializers.ModelSerializer):
    """
    Serializer class for displaying detailed information, used in UserDetailAPIView.
    """

    class Meta:
        model = User
        fields = "__all__"
