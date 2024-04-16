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
from typing import Optional

from .base import BaseIO
from .moderation import CLIPAndModerationIO


class AppStageIO(BaseIO):
    """
    IO class for app stages.

    Args:
        io: (`BaseIO`)
            The output of the app stage.
        name: (`str`)
            The name of the output
    """

    io: Optional[BaseIO]
    name: str


class AppIO(BaseIO):
    """
    IO class for an app.

    Args:
        io: (`BaseIO`)
            The output of the app stage.
        moderation: (`CLIPAndModerationIO`)
            The moderation output on the
            output io.
    """

    io: BaseIO
    moderation: CLIPAndModerationIO
