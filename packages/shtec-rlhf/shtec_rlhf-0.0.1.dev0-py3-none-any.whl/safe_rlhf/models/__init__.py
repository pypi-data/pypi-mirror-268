#******************************************************************************************************** 
#  @author	     tcexeexe
#  @date         04,2024
#
#  @par     Copyright (c) 2024, SHTEC
# 
# *******************************************************************************************************/
"""Utility functions for Hugging Face auto-models."""

from shtec_rlhf.models.pretrained import load_pretrained_models
from shtec_rlhf.models.score_model import AutoModelForScore, ScoreModelOutput


__all__ = ['load_pretrained_models', 'AutoModelForScore', 'ScoreModelOutput']
