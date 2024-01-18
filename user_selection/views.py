from rest_framework import generics

from user_selection.models import User
from user_selection.serializers import CreateUserSerializer
from user_selection.serializers import UserRetrieveSerializers


class UserCreateAPIView(generics.CreateAPIView):
    """
    Controller for creating new users.
    """

    serializer_class = CreateUserSerializer


class UserDetailAPIView(generics.RetrieveAPIView):
    """
    Controller allows to retrieve detailed information about the specified user.
    """

    serializer_class = UserRetrieveSerializers
    queryset = User.objects.all()
