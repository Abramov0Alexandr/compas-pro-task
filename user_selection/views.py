from rest_framework import generics

from user_selection.models import User
from user_selection.serializers import CreateUserSerializer
from user_selection.serializers import UserRetrieveSerializers


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = CreateUserSerializer


class UserDetailAPIView(generics.RetrieveAPIView):
    serializer_class = UserRetrieveSerializers
    queryset = User.objects.all()
