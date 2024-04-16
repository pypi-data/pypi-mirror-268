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
import itertools
from statistics import mean
from typing import Optional, List, Dict

from pydantic import BaseModel

from .run import AppRunResult


class AppTestModerationResult(BaseModel):
    is_nsfw: bool
    is_forbidden: bool
    concepts: List[str]


class AppTestResult(BaseModel):
    data: List[AppRunResult]
    moderation: AppTestModerationResult
    average_duration: float
    average_embedding: List[float]

    @classmethod
    def from_app_run_results(cls, results: List[AppRunResult]) -> "AppTestResult":
        import numpy as np

        # resize
        return cls(
            data=results,
            average_duration=mean([res.duration for res in results[1:]])
            if len(results) > 1
            else results[0].duration,
            average_embedding=np.mean(
                np.array([res.data.embedding for res in results]), axis=0
            ).tolist(),
            moderation=AppTestModerationResult(
                is_nsfw=any([res.data.moderation.is_nsfw for res in results]),
                is_forbidden=any([res.data.moderation.is_forbidden for res in results]),
                concepts=list(
                    set(
                        itertools.chain.from_iterable(
                            res.data.moderation.concepts.keys() for res in results
                        )
                    )
                ),
            ),
        )


class AppTestData(BaseModel):
    config: Dict
    callback_url: Optional[str] = None
