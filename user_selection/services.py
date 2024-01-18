from typing import TYPE_CHECKING
from PIL import Image


if TYPE_CHECKING:
    from user_selection.models import User


def user_avatar_upload_path(model: 'User', file: Image) -> str:
    return f"user_selection/{model.pk}/{file}"
