"""
scmopy: Distribution-Agnostic Structural Causal Models Optimization in Python

scmopy is a comprehensive package for causal discovery/analysis using several novel types of SCM Optimization algorithms.
The package also incorporates Distribution-Agnostic methods for causal estimation, which enables deviations from the necessity of any specific distributional assumption.

Should you use the scmopy package, please cite the following:
- Lee, Sanghoon (2024). ESA-2SCM for Causal Discovery: Causal Modeling with Elastic Segmentation-based Synthetic Instrumental Variable, SnB Political and Economic Research Institute, 1, 21. <snbperi.org/article/230>.
- S.Shimizu and Y.Kano (2008). Use of non-normality in structural equation modeling: Application to direction of causation, Journal of Statistical Planning and Inference, 138, 11, 3483-3491.


   Copyright 2024 Sanghoon Lee (DSsoli). All Rights Reserved.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
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