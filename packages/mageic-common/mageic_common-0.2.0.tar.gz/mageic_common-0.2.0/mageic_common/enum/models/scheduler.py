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


class Scheduler(str, Enum):
    """
    Enum for model schedulers.
    """

    LCM = "lcm"
    DDIM = "ddim"
    DDPM = "ddpm"
    DEIS = "deis"
    DPMM = "dpmm"
    DPMM_SDE = "dpmm_sde"
    DPMM_SDE_KARRAS = "dpmm_sde_karras"
    DPMM_KARRAS = "dpmm_karras"
    DPMS = "dpms"
    DPMS_KARRAS = "dpms_karras"
    DPM_SDE = "dpm_sde"
    EULER = "euler"
    EULERA = "eulera"
    HEUN = "heun"
    KDPM2 = "kdpm2"
    KDPM2_KARRAS = "kdpm2_karras"
    KDPM2A = "kdpm2a"
    KDPM2A_KARRAS = "kdpm2a_karras"
    LMS = "lms"
    LMS_KARRAS = "lms_karras"
    PNDM = "pndm"
    UNIPC = "unipc"
