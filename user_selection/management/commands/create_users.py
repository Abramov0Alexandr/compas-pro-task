import os

from django.core.management.base import BaseCommand
from django.core.management.base import CommandError

from user_selection.models import User


class Command(BaseCommand):
    help = "A custom command to create users of each role type"

    def handle(self, *args, **options):
        try:

            roles: dict[str, str] = User.USER_ROLE_CHOICE
            role_avatar_mapping = {
                "user": "user.png",
                "manager": "admin.png",
                "crm-admin": "crm_admin.png",
            }

            avatar_path = "user_selection/avatars/default_avatars/"
            User.objects.all().delete()

            for role in roles.keys():
                email: str = f"{role}@example.com"
                password: str = f"{role}123321"

                User.objects.filter(email=email).delete()

                avatar_filename = role_avatar_mapping[role]
                avatar_full_path = os.path.join(avatar_path, avatar_filename)

                User.objects.create_user(
                    email=email,
                    password=password,
                    role_choice=role,
                    avatar=avatar_full_path,
                )

                self.stdout.write(
                    self.style.SUCCESS(f"Successfully created user with role {role}")
                )

        except User.DoesNotExist:
            raise CommandError(
                "User model does not exist. Make sure you applied migrations"
            )
