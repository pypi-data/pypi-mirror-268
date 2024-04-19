#******************************************************************************************************** 
#  @author	     tcexeexe
#  @date         04,2024
#
#  @par     Copyright (c) 2024, SHTEC
# 
# *******************************************************************************************************/
"""The main training script to supervised finetune a model."""

import sys

from shtec_rlhf.finetune.main import main


if __name__ == '__main__':
    sys.exit(main())
