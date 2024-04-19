#******************************************************************************************************** 
#  @author	     tcexeexe
#  @date         04,2024
#
#  @par     Copyright (c) 2024, SHTEC
# 
# *******************************************************************************************************/
"""The main training script to train Safe-RLHF using PPO algorithm with reward shaping."""

import sys

from shtec_rlhf.algorithms.ppo_reward_shaping.main import main


if __name__ == '__main__':
    sys.exit(main())
