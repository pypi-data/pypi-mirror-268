#******************************************************************************************************** 
#  @author	     tcexeexe
#  @date         04,2024
#
#  @par     Copyright (c) 2024, SHTEC
# 
# *******************************************************************************************************/

from __future__ import annotations

import torch
from torch.nn.utils.rnn import pad_sequence
from torch.types import Number

from shtec_rlhf.configs import PROMPT_ASSISTANT, PROMPT_BEGIN, PROMPT_USER


def format_prompt(
    input: str | list[str],  # pylint: disable=redefined-builtin
    eos_token: str,
) -> str:
    if isinstance(input, str):
        input = [input]
    elif not isinstance(input, list):
        raise ValueError(f'Unsupported type of `input`: {type(input)}. Expected: str or list[str].')

    if len(input) % 2 != 1:
        raise ValueError(
            'The length of `input` must be odd, while `input` must end at the user question.',
        )

    buffer = [PROMPT_BEGIN]
    for i, line in enumerate(input):
        if i % 2 == 0:
            # User input
            buffer.extend((PROMPT_USER.format(input=line), PROMPT_ASSISTANT))
        else:
            # Assistant response
            buffer.extend((line, eos_token))

    return ''.join(buffer)


def right_padding(sequences: list[torch.Tensor], padding_value: Number) -> torch.Tensor:
    return pad_sequence(sequences, batch_first=True, padding_value=padding_value)


def left_padding(sequences: list[torch.Tensor], padding_value: Number) -> torch.Tensor:
    return right_padding(
        [seq.flip(0) for seq in sequences],
        padding_value=padding_value,
    ).flip(1)
