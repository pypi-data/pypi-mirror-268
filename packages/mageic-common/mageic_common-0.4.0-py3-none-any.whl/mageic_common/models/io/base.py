#
#
#   _____ _____     ____   ____        _________________    ____  ____
#  /     \\__  \   / ___\_/ __ \      /  ___/\____ \__  \ _/ ___\/ __ \
# |  Y Y  \/ __ \_/ /_/  >  ___/      \___ \ |  |_> > __ \\  \__\  ___/
# |__|_|  (____  /\___  / \___  > /\ /____  >|   __(____  /\___  >___  >
#       \/     \//_____/      \/  \/      \/ |__|       \/     \/    \/
#
# Copyright (C) (2024) Ollano, Inc. - All Rights Reserved
#
from pydantic import BaseModel, ConfigDict

from PIL.Image import Image as ImageType


class BaseIO(BaseModel):
    """
    Base IO class.
    """

    pass


class TextIO(BaseIO):
    """
    IO class for text apps.

    Args:
        text (`str`)
            The textual IO.
    """

    text: str


class ImageIO(BaseIO):
    """
    IO class for image apps.

    Args:
        image (`PIL.Image.Image`)
            A PIL Image.
    """

    model_config = ConfigDict(arbitrary_types_allowed=True)

    image: ImageType
