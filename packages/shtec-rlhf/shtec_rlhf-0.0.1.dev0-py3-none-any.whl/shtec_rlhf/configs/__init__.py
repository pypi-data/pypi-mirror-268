#******************************************************************************************************** 
#  @author	     tcexeexe
#  @date         04,2024
#
#  @par     Copyright (c) 2024, SHTEC
# 
# *******************************************************************************************************/
"""Configurations and constants."""

from shtec_rlhf.configs import constants
from shtec_rlhf.configs.constants import *  # noqa: F403
from shtec_rlhf.configs.deepspeed_config import (
    TEMPLATE_DIR,
    get_deepspeed_eval_config,
    get_deepspeed_train_config,
)


__all__ = [
    *constants.__all__,
    'TEMPLATE_DIR',
    'get_deepspeed_eval_config',
    'get_deepspeed_train_config',
]
