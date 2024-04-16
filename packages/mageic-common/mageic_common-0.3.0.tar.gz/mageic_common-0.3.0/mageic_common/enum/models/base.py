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
from enum import Enum


class ModelArchitecture(str, Enum):
    """
    Enum for model architectures.
    """

    SD_V15 = "sd-v1-5"
    SDXL = "sdxl"


class ModelType(str, Enum):
    """
    Enum for model types.
    """

    BASE = "base"
    LORA = "lora"
    TI = "ti"
    CONTROLNET = "controlnet"
