from typing import TYPE_CHECKING

from PIL import Image


if TYPE_CHECKING:
    from user_selection.models import User


def user_avatar_upload_path(model: "User", file: Image) -> str:
    """
    Services function for uploading user's avatar.
    :param model: model information, with used to compose the load path.
    :param file: image file.
    :return: path with will be used to upload.
    """

    return f"user_selection/avatars/{model.email}/{file}"
