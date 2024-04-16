#******************************************************************************************************** 
#  @author	     tcexeexe
#  @date         04,2024
#
#  @par     Copyright (c) 2024, SHTEC
# 
# *******************************************************************************************************/
"""Dataset classes."""

from __future__ import annotations

from typing import Dict

import torch
from torch.utils.data import Dataset

from shtec_rlhf.datasets import raw
from shtec_rlhf.datasets.base import (
    CollatorBase,
    RawDataset,
    RawSample,
    TokenizedDataset,
    parse_dataset,
)
from shtec_rlhf.datasets.preference import (
    PreferenceBatch,
    PreferenceCollator,
    PreferenceDataset,
    PreferenceSample,
)
from shtec_rlhf.datasets.prompt_only import (
    PromptOnlyBatch,
    PromptOnlyCollator,
    PromptOnlyDataset,
    PromptOnlySample,
)
from shtec_rlhf.datasets.raw import *  # noqa: F403
from shtec_rlhf.datasets.safety_preference import (
    SafetyPreferenceBatch,
    SafetyPreferenceCollator,
    SafetyPreferenceDataset,
    SafetyPreferenceSample,
)
from shtec_rlhf.datasets.supervised import (
    SupervisedBatch,
    SupervisedCollator,
    SupervisedDataset,
    SupervisedSample,
)


__all__ = [
    'DummyDataset',
    'parse_dataset',
    'RawDataset',
    'RawSample',
    'TokenizedDataset',
    'CollatorBase',
    'PreferenceDataset',
    'PreferenceSample',
    'PreferenceBatch',
    'PreferenceCollator',
    'PromptOnlyDataset',
    'PromptOnlyCollator',
    'PromptOnlySample',
    'PromptOnlyBatch',
    'SafetyPreferenceDataset',
    'SafetyPreferenceCollator',
    'SafetyPreferenceSample',
    'SafetyPreferenceBatch',
    'SupervisedDataset',
    'SupervisedCollator',
    'SupervisedSample',
    'SupervisedBatch',
    *raw.__all__,
]


class DummyDataset(Dataset[Dict[str, torch.Tensor]]):
    def __init__(self, length: int) -> None:
        self.length = length

    def __len__(self) -> int:
        return self.length

    def __getitem__(self, index: int) -> dict[str, torch.Tensor]:
        return {}
