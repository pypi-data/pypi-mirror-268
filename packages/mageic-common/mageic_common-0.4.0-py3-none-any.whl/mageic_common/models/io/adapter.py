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
from typing import Optional, List
from pydantic import ConfigDict
from PIL.Image import Image as ImageType

from mageic_common.enum.models import IPAdapter
from .base import BaseIO


class ImageAdapterIO(BaseIO):
    """
    IO class for image adapters.

    Args:
        image (`PIL.Image.Image`)
            A PIL Image.
        weight (`float`)
            The weight of the adapter
        adapter_type (`IPAdapter`)
            The type of adapter
        mask (`PIL.Image.Image`)
            The mask image
        is_mask_required (`bool`)
            Boolean indicating if mask is required
    """

    model_config = ConfigDict(arbitrary_types_allowed=True)

    image: List[ImageType]
    weight: float
    adapter_type: IPAdapter
    mask: Optional[ImageType] = None
    is_mask_required: bool = False


class MultiImageAdapterIO(BaseIO):
    """
    IO class for multiple image adapters.

    Args:
        adapters (`List[ImageAdapterIO]`)
            List of image adapters.
    """

    model_config = ConfigDict(arbitrary_types_allowed=True)

    adapters: List[ImageAdapterIO]
