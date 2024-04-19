#******************************************************************************************************** 
#  @author	     tcexeexe
#  @date         04,2024
#
#  @par     Copyright (c) 2024, SHTEC
# 
# *******************************************************************************************************/
"""Firefly (流萤) dataset for supervised instruction fine-tuning."""

from __future__ import annotations

from datasets import load_dataset
from shtec_rlhf.datasets.base import RawDataset, RawSample


__all__ = ['FireflyDataset']


class FireflyDataset(RawDataset):
    NAME: str = 'firefly'

    def __init__(self, path: str | None = None) -> None:
        self.data = load_dataset(path or 'YeungNLP/firefly-train-1.1M', split='train')

    def __getitem__(self, index: int) -> RawSample:
        data = self.data[index]
        return RawSample(input=data['input'], answer=data['target'])

    def __len__(self) -> int:
        return len(self.data)
