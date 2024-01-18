from django.urls import path
from django.views.decorators.cache import cache_page

from user_selection.apps import UserSelectionConfig
from user_selection.views import UserCreateAPIView
from user_selection.views import UserDetailAPIView

app_name = UserSelectionConfig.name

urlpatterns = [
    path("create/", UserCreateAPIView.as_view(), name="user_create"),
    path("<int:pk>/", cache_page(60)(UserDetailAPIView.as_view()), name="user_detail"),
]
