from django.urls import path

from user_selection.apps import UserSelectionConfig
from user_selection.views import UserCreateAPIView
from user_selection.views import UserDetailAPIView

app_name = UserSelectionConfig.name

urlpatterns = [
    path("create/", UserCreateAPIView.as_view(), name="user_create"),
    path("<int:pk>/", UserDetailAPIView.as_view(), name="user_detail"),
]
