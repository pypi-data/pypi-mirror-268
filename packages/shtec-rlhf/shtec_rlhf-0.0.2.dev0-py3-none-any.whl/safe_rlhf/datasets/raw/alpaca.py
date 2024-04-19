#******************************************************************************************************** 
#  @author	     tcexeexe
#  @date         04,2024
#
#  @par     Copyright (c) 2024, SHTEC
# 
# *******************************************************************************************************/
"""Stanford Alpaca dataset for supervised instruction fine-tuning."""

from __future__ import annotations

from datasets import load_dataset
from shtec_rlhf.datasets.base import RawDataset, RawSample


__all__ = ['AlpacaDataset']


class AlpacaDataset(RawDataset):
    NAME: str = 'alpaca'
    ALIASES: tuple[str, ...] = ('stanford-alpaca',)

    def __init__(self, path: str | None = None) -> None:
        self.data = load_dataset(path or 'tatsu-lab/alpaca', split='train')

    def __getitem__(self, index: int) -> RawSample:
        data = self.data[index]
        input = (  # pylint: disable=redefined-builtin
            ' '.join((data['instruction'], data['input'])) if data['input'] else data['instruction']
        )
        answer = data['output']
        return RawSample(input=input, answer=answer)

    def __len__(self) -> int:
        return len(self.data)
