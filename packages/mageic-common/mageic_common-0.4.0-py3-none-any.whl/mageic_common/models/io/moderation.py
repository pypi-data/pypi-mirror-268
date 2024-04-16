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
from typing import List, Dict
import numpy as np
from pydantic import ConfigDict

from .base import BaseIO


class ModerationInstanceIO(BaseIO):
    """
    Single moderation IO instance.
    Args:
        text (`str`)
            The concept string.
        score (`float`)
            The concept CLIP score.
    """

    text: str
    score: float


class ModerationIO(BaseIO):
    """
    IO class for moderation apps.

    Args:
        is_nsfw (`bool`)
            Boolean indicating if NSFW content is detected.
        is_forbidden (`bool`)
            Boolean indicating if forbidden content is detected.
        concepts (`dict`)
            Dict containing the details of the moderation
            concepts found, if any.
    """

    is_nsfw: bool
    is_forbidden: bool
    concepts: Dict[str, List[ModerationInstanceIO]]


class CLIPAndModerationIO(BaseIO):
    """
    IO class for moderation apps.

    Args:
        embedding (`np.ndarray`)
            Numpy array of the CLIP embedding.
        moderation (`ModerationIO`)
            Moderation details.
    """

    model_config = ConfigDict(arbitrary_types_allowed=True)

    embedding: np.ndarray
    moderation: ModerationIO
