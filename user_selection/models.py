from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from user_selection.services import user_avatar_upload_path
from user_selection.user_manager import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    USER_ROLE_CHOICE = {
        "user": "Пользователь",
        "manager": "Менеджер",
        "crm-admin": "CRM-администратор",
    }

    email = models.EmailField(unique=True)
    role_choice = models.CharField(
        max_length=20, choices=USER_ROLE_CHOICE, default="user"
    )
    offer = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to=user_avatar_upload_path, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.email}: {self.role_choice} {self.offer}"

    @property
    def is_staff(self):
        return self.is_superuser

    class Meta:
        ordering = ("pk",)
