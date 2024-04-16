#******************************************************************************************************** 
#  @author	     tcexeexe
#  @date         04,2024
#
#  @par     Copyright (c) 2024, SHTEC
# 
# *******************************************************************************************************/
"""The main training script to run the DPO algorithm."""

import sys

from shtec_rlhf.algorithms.dpo.main import main


if __name__ == '__main__':
    sys.exit(main())
