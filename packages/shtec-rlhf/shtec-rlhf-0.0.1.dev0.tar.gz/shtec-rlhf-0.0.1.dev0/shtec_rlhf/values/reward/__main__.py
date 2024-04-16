#******************************************************************************************************** 
#  @author	     tcexeexe
#  @date         04,2024
#
#  @par     Copyright (c) 2024, SHTEC
# 
# *******************************************************************************************************/
"""The main training script to train a reward model in shtec-rlhf."""

import sys

from shtec_rlhf.values.reward.main import main


if __name__ == '__main__':
    sys.exit(main())
