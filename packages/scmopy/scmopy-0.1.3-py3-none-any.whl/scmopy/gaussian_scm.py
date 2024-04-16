"""

scmopy: Distribution-Agnostic Structural Causal Models Optimization in Python

The scmopy package is a composite package for causal discovery/analysis using several novel types of SCM Optimization algorithms.
The package also incorporates Distribution-Agnostic methods for causal estimation, which enables deviations from the necessity of any specific distributional assumption.

Should you use the scmopy package, please cite the following articles.
- Lee, Sanghoon (2024). ESA-2SCM for Causal Discovery: Causal Modeling with Elastic Segmentation-based Synthetic Instrumental Variable, SnB Political and Economic Research Institute, 1, 21. <snbperi.org/article/230>.
- S.Shimizu and Y.Kano (2008). Use of non-normality in structural equation modeling: Application to direction of causation, Journal of Statistical Planning and Inference, 138, 11, 3483-3491.

"""


import numpy as np
import pandas as pd
from .components import SynIV, r2_score
from .base import BaseCM


class Esa2Scm(BaseCM):
    
    def __init__(self, x1, x2, prior_knowledge=None):
        super().__init__(x1, x2, prior_knowledge)


    @staticmethod
    def _estimate(x, z):
        if np.var(z, ddof=1) == 0:
            b = 0
        else:  
            b = np.cov(x, z)[0,1] / np.var(z, ddof=1)
        c = np.mean(x) - b * np.mean(z)
        x_hat = c + b * z
        return x_hat, b
    
    
    def fit(self, syniv_method: str = "esa", **kwargs):
        
        if self._prior_knowledge is not None:
            
            def estimate(x1, x2, prior_knowledge):
                x_hat, b = Esa2Scm._estimate(x1, x2)
                causal_dir = prior_knowledge
                score = r2_score(x1, x_hat)
                return x_hat, b, causal_dir, score
                        
            if self._prior_knowledge == 'x2->x1':
                self._x_hat, self._b, self._causal_dir_fixed, self._determined_mod_ols_score = estimate(self._x1, self._x2, self._prior_knowledge)
                
            else:
                self._x_hat, self._b, self._causal_dir_fixed, self._determined_mod_ols_score = estimate(self._x2, self._x1, self._prior_knowledge)

        else:
            estimate_syniv = SynIV.get_syniv(syniv_method)
            self._z1, self._z2 = estimate_syniv(self._x1, **kwargs), estimate_syniv(self._x2, **kwargs)
            
            self._x1_iv1sls, self._x2_iv1sls = Esa2Scm._estimate(self._x1, self._z1)[0], Esa2Scm._estimate(self._x2, self._z2)[0]
            self._x1_slsiv_corr_ = 'undefined (0 variance)' if np.var(self._x1_iv1sls) == 0 or np.var(self._x1) == 0 else np.corrcoef(self._x1_iv1sls, self._x1)[0][1] 
            self._x2_slsiv_corr_ = 'undefined (0 variance)' if np.var(self._x2_iv1sls) == 0 or np.var(self._x2) == 0 else np.corrcoef(self._x2_iv1sls, self._x2)[0][1]
            
            self._x1_iv2sls, self._b12 = Esa2Scm._estimate(self._x1, self._x2_iv1sls)
            self._x2_iv2sls, self._b21 = Esa2Scm._estimate(self._x2, self._x1_iv1sls)
            
            self._score, self._score_rev = round(r2_score(self._x1, self._x1_iv2sls), 5), round(r2_score(self._x2, self._x2_iv2sls), 5) 
            
            self._causal_dir = "x2->x1" if self._score > self._score_rev else "x1->x2" if self._score < self._score_rev else "undetermined"
            
            if self._causal_dir == "x2->x1":
                self._true_x_hat, self._true_causal_coef, self._true_score = self._x2_iv2sls, self._b12, self._score
                self._determined_mod_ols_score = round(r2_score(self._x1, Esa2Scm._estimate(self._x1, self._x2)[0]), 5) 
                
            elif self._causal_dir == "x1->x2":
                self._true_x_hat, self._true_causal_coef, self._true_score = self._x1_iv2sls, self._b21, self._score_rev
                self._determined_mod_ols_score = round(r2_score(self._x2, Esa2Scm._estimate(self._x2, self._x1)[0]), 5) 
                
            else:
                self._true_x_hat, self._true_causal_coef, self._true_score, self._determined_mod_ols_score = np.nan, 0, 0, 0
            
        return self
    
    
    def _summary(self):
        summary_idx = ["Causal Direction", "Causal Coefficient", "Goodness of Fit"]
        additional_idx = ["Corr (2SLS_IV-Explanatory)", "Posthoc Goodness of Fit"]
        
        if self._prior_knowledge is not None:
            self._result = pd.DataFrame({self._prior_knowledge + " (Predetermined)": [self._prior_knowledge, self._b, self._determined_mod_ols_score]}, index=summary_idx)
            return self._result
        
        summary_columns = ['x2->x1', 'x1->x2']
        summary_values = [str(self._causal_dir == 'x2->x1'), self._b12, self._score, self._x2_slsiv_corr_, [self._determined_mod_ols_score if self._causal_dir == 'x2->x1' else '-'][0]]
        summary_values_rev = [str(self._causal_dir == 'x1->x2'), self._b21, self._score_rev, self._x1_slsiv_corr_, [self._determined_mod_ols_score if self._causal_dir == 'x1->x2' else '-'][0]]
        self._result = pd.DataFrame({summary_columns[0]: summary_values, summary_columns[1]: summary_values_rev}, index=summary_idx+additional_idx)
        
        return self._result
    
    
    @property
    def x1(self):
        return self._x1
    
    @property
    def x2(self):
        return self._x2
    
    @property
    def z1(self):
        if hasattr(self, "_z1"):
            return self._z1
        raise AttributeError("Synthetic IV (z1) is not generated as Prior Knowledge has been set")
    
    @property
    def z2(self):
        if hasattr(self, "_z2"):
            return self._z2
        raise AttributeError("Synthetic IV (z2) is not generated as Prior Knowledge has been set")
    
    @property
    def causal_coef(self):
        if hasattr(self, "_b"):
            return self._b
        return self._true_causal_coef
    
    @property
    def causal_direction(self):
        if hasattr(self, "_causal_dir_fixed"):
            return self._causal_dir_fixed + ' (prior knowledge)'
        return self._causal_dir
    
    @property
    def esa2scm_score(self):
        if hasattr(self, "_true_score"):
            return self._true_score
        raise AttributeError("esa2scm_score is not unavailable as Pior Knowledge has been set")
    
    @property
    def posthoc_score(self):
        return self._determined_mod_ols_score
    
    @property
    def x_hat(self):
        if hasattr(self, "_x_hat"):
            return self._x_hat
        return self._true_x_hat
    
    @property
    def corr_x1_to_slsiv(self):
        if hasattr(self, "_x1_slsiv_corr_"):
            return self._x1_slsiv_corr_
        raise AttributeError("Synthetic IV to calculate correlation coefficient is not generated as Prior knowledge has been set")
    
    @property
    def corr_x2_to_slsiv(self):
        if hasattr(self, "_x2_slsiv_corr_"):
            return self._x2_slsiv_corr_
        raise AttributeError("Synthetic IV to calculate correlation coefficient is not generated as Prior knowledge has been set")
    
    @property
    def summary(self):
        return self._summary
    
