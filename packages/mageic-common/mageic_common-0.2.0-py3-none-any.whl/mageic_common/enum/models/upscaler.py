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


class Upscaler(str, Enum):
    """
    Enum for upscalers.
    """

    R_ESRGAN_X2 = "real-esrgan-x2"
    R_ESRGAN_X4 = "real-esrgan-x4"
    R_ESRGAN_X4_ANIME = "real-esrgan-x4-anime"

    R_ESRGAN_X2_GFPGAN = "real-esrgan-x2-gfpgan"
    R_ESRGAN_X4_GFPGAN = "real-esrgan-x4-gfpgan"
    R_ESRGAN_X4_ANIME_GFPGAN = "real-esrgan-x4-anime-gfpgan"

    R_ESRGAN_X2_RFORMER = "real-esrgan-x2-rformer"
    R_ESRGAN_X4_RFORMER = "real-esrgan-x4-rformer"
    R_ESRGAN_X4_ANIME_RFORMER = "real-esrgan-x4-anime-rformer"

    R_ESRGAN_X2_CFORMER = "real-esrgan-x2-cformer"
    R_ESRGAN_X4_CFORMER = "real-esrgan-x4-cformer"
    R_ESRGAN_X4_ANIME_CFORMER = "real-esrgan-x4-anime-cformer"

    LANCZOS = "lanczos"


class UpscalerModel(str, Enum):
    """
    Enum for upscaler models.
    """

    ESRGAN_X2 = "esrgan-x2"
    ESRGAN_X4 = "esrgan-x4"
    ESRGAN_X4_ANIME = "esrgan-x4-anime"
    GFPGAN = "gfpgan"
    RFORMER = "rformer"  # restoreformer
    CFORMER = "cformer"  # codeformer
