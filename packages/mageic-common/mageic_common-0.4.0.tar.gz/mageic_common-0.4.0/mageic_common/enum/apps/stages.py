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

STAGE_TYPE_KEY = "id"


class StageType(str, Enum):
    PROMPT = "prompt"
    IMAGE = "image"
    PROMPT_ENHANCE = "prompt-enhance"
    T2I = "t2i"
    RESIZE = "resize"
    UPSCALE = "upscale"
    HIRES_UPSCALE = "hires-upscale"
    I2I = "i2i"
    SELFIE = "selfie"
    REFINER = "refiner"
    I2V = "i2v"
    ADAPTER = "adapter"
    DYNAMIC_ADAPTER = "dynamic-adapter"
    CONTROLNET = "controlnet"
    DYNAMIC_CONTROLNET = "dynamic-controlnet"
