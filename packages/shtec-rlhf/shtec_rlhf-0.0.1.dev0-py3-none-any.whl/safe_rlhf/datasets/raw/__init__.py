#******************************************************************************************************** 
#  @author	     tcexeexe
#  @date         04,2024
#
#  @par     Copyright (c) 2024, SHTEC
# 
# *******************************************************************************************************/
"""Raw datasets."""

from shtec_rlhf.datasets.raw.alpaca import AlpacaDataset
from shtec_rlhf.datasets.raw.firefly import FireflyDataset
from shtec_rlhf.datasets.raw.hh_rlhf import (
    HhRLHFDialogueDataset,
    HhRLHFHarmlessDialogueDataset,
    HhRLHFHelpfulDialogueDataset,
)
from shtec_rlhf.datasets.raw.moss import MOSS002SFT, MOSS003SFT
from shtec_rlhf.datasets.raw.shtec_rlhf import (
    SafeRLHF10KTrainDataset,
    SafeRLHF30KTestDataset,
    SafeRLHF30KTrainDataset,
    SafeRLHFDataset,
    SafeRLHFTestDataset,
    SafeRLHFTrainDataset,
)


__all__ = [
    'AlpacaDataset',
    'FireflyDataset',
    'HhRLHFDialogueDataset',
    'HhRLHFHarmlessDialogueDataset',
    'HhRLHFHelpfulDialogueDataset',
    'MOSS002SFT',
    'MOSS003SFT',
    'SafeRLHFDataset',
    'SafeRLHFTrainDataset',
    'SafeRLHFTestDataset',
    'SafeRLHF30KTrainDataset',
    'SafeRLHF30KTestDataset',
    'SafeRLHF10KTrainDataset',
]
