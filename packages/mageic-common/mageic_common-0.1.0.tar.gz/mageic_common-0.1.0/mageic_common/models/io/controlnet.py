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
from typing import List
from pydantic import ConfigDict
from PIL.Image import Image as ImageType

from mageic_common.enum.models.controlnet import Controlnet

from .base import BaseIO


class ControlnetIO(BaseIO):
    """
    IO class for controlnets.

    Args:
        image (`PIL.Image.Image`)
            The controlnet conditioning image.
        weight (`float`)
            The weight of the controlnet.
        controlnet_type (`Controlnet`)
            The type of controlnet.
    """

    model_config = ConfigDict(arbitrary_types_allowed=True)
    image: ImageType
    weight: float
    controlnet_type: Controlnet


class MultiControlnetIO(BaseIO):
    """
    IO class for multiple controlnets.

    Args:
        controlnets (`List[ControlnetIO]`)
            List of controlnets.
    """

    model_config = ConfigDict(arbitrary_types_allowed=True)

    controlnets: List[ControlnetIO]
