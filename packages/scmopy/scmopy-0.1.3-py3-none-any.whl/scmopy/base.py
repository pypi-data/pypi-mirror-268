"""

scmopy: Distribution-Agnostic Structural Causal Models Optimization in Python

The scmopy package is a composite package for causal discovery/analysis using several novel types of SCM Optimization algorithms.
The package also incorporates Distribution-Agnostic methods for causal estimation, which enables deviations from the necessity of any specific distributional assumption.

Should you use the scmopy package, please cite the following articles.
- Lee, Sanghoon (2024). ESA-2SCM for Causal Discovery: Causal Modeling with Elastic Segmentation-based Synthetic Instrumental Variable, SnB Political and Economic Research Institute, 1, 21. <snbperi.org/article/230>.
- S.Shimizu and Y.Kano (2008). Use of non-normality in structural equation modeling: Application to direction of causation, Journal of Statistical Planning and Inference, 138, 11, 3483-3491.

"""


from typing import Union, List
import numpy as np
import pandas as pd


class BaseCM:
    
    _KNOWLEDGE = (None, 'x2->x1', 'x1->x2')
    
    def __init__(
        self, 
        x1: Union[np.ndarray, pd.Series, List], 
        x2: Union[np.ndarray, pd.Series, List],
        prior_knowledge: str = None,
        ):
        
        if np.ndim(x1) > 1 or np.ndim(x2) > 1:
            raise ValueError("Inputs for x1 and x2 must be 1-Dimensional")
        
        if len(x1) != len(x2):
            raise ValueError("Need equal sample sizes for x1 and x2")
        
        try: check_x1, check_x2 = np.array(x1, dtype=float), np.array(x2, dtype=float)
        except ValueError as e:
            raise ValueError("Inputs contain non-numerical values") from None
        
        if np.isnan(check_x1).any() or np.isnan(check_x2).any():
            raise ValueError("Inputs contain NaN values")
        
        if prior_knowledge in BaseCM._KNOWLEDGE:
            self._prior_knowledge = prior_knowledge
        else: raise ValueError("Valid expression for prior_knowledge: 'x2->x1' or 'x1->x2'")
        
        self._x1, self._x2 = np.array(x1) , np.array(x2)