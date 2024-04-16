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
import io
import base64
from pydantic import BaseModel
from typing import Optional, List, Dict

from PIL import ImageOps

from mageic_common.models.io import ModerationIO, AppIO


class AppRunImageResultData(BaseModel):
    image: str
    moderation: ModerationIO
    embedding: List[float]

    @classmethod
    def from_app_io(
        cls, app_io: AppIO, contain_size: Optional[int] = None
    ) -> "AppRunImageResultData":
        # image
        image = app_io.io.io.image
        if contain_size is not None:
            image = ImageOps.contain(image, (contain_size, contain_size))

        # save
        buffered = io.BytesIO()
        image.save(
            buffered,
            format="JPEG",
            quality="web_maximum",
            optimize=True,
        )
        image_b64 = (
            f"data:image/jpeg;base64,{base64.b64encode(buffered.getvalue()).decode()}"
        )

        return cls(
            image=image_b64,
            moderation=app_io.moderation.moderation,
            embedding=app_io.moderation.embedding.tolist(),
        )


class AppRunResult(BaseModel):
    type: str
    duration: float
    data: AppRunImageResultData

    @classmethod
    def from_app_io(
        cls, app_io: AppIO, duration: float, contain_size: Optional[int] = None
    ) -> "AppRunResult":
        return cls(
            type="image",
            duration=duration,
            data=AppRunImageResultData.from_app_io(
                app_io=app_io,
                contain_size=contain_size,
            ),
        )


class AppRunData(BaseModel):
    config: Dict
    callback_url: Optional[str] = None
