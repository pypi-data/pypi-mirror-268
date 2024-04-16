"""

scmopy: Distribution-Agnostic Structural Causal Models Optimization in Python

The scmopy package is a composite package for causal discovery/analysis using several novel types of SCM Optimization algorithms.
The package also incorporates Distribution-Agnostic methods for causal estimation, which enables deviations from the necessity of any specific distributional assumption.

Should you use the scmopy package, please cite the following articles.
- Lee, Sanghoon (2024). ESA-2SCM for Causal Discovery: Causal Modeling with Elastic Segmentation-based Synthetic Instrumental Variable, SnB Political and Economic Research Institute, 1, 21. <snbperi.org/article/230>.
- S.Shimizu and Y.Kano (2008). Use of non-normality in structural equation modeling: Application to direction of causation, Journal of Statistical Planning and Inference, 138, 11, 3483-3491.

"""


from scipy.stats import kstest, shapiro, anderson, normaltest, linregress
import numpy as np
from .base import BaseCM
from .gaussian_scm import Esa2Scm
from .nongaussian_scm import GradientNonGaussianScm


class ScmSelector(BaseCM):
        
    def __init__(self, x1, x2, prior_knowledge=None):
        super().__init__(x1, x2, prior_knowledge)
        self._is_fitted = False

    
    @staticmethod    
    def _ks_test(e, alpha=0.15):
        p_val = kstest(e, cdf='norm', args=(np.mean(e), np.std(e, ddof=1)))[1]
        reject_H0 = p_val < alpha 
        
        return reject_H0 # If True, non-gaussian
    

    @staticmethod
    def _sw_test(e, alpha=0.15):
        p_val = shapiro(e)[1]
        reject_H0 = p_val < alpha
        
        return reject_H0 # If true, non-gaussian


    @staticmethod
    def _anderson_test(e, alpha=0.15):
        valid_alpha = [0.15, 0.1, 0.05, 0.025, 0.01]
        
        if alpha not in valid_alpha:
            raise ValueError(f"valid alpha choice: {valid_alpha}")
        
        alpha_percent = alpha * 100
        
        anderson_res = anderson(e, 'norm')
        
        idx = np.where(anderson_res[2]==alpha_percent)[0][0]
        reject_H0 = anderson_res[0] > anderson_res[1][idx]
        
        return reject_H0 # If true, non-gaussian


    @staticmethod
    def _dp_test(e, alpha=0.15):
        p_val = normaltest(e).pvalue
        reject_H0 = p_val < alpha
        
        return reject_H0 # If True, non-gaussian
    



    def fit(self, alpha: float = 0.15, voting_strategy: str = 'strict') -> None:
        
        valid_alpha = [0.15, 0.1, 0.05, 0.025, 0.01]
        
        if alpha not in valid_alpha:
            raise ValueError(f"valid alpha choice: {valid_alpha}")

        vote_thres = {'strict':1, 'moderate': 2, 'soft': 3}
        
        if voting_strategy not in vote_thres.keys():
            raise ValueError("available voting strategy: 'strict', 'moderate', 'soft'")
        
        if self._prior_knowledge is not None:
            if self._prior_knowledge == 'x2->x1':
                mod = linregress(self._x2, self._x1)
                resid = self._x1 - (mod.slope * self._x2 + mod.intercept)
            else: 
                mod = linregress(self._x1, self._x2)
                resid = self._x2 - (mod.slope * self._x1 + mod.intercept)    
            e_list = [resid]
        
        else:
            mod1 = linregress(self._x2, self._x1)
            resid1 = self._x1 - (mod1.slope * self._x2 + mod1.intercept)
            
            mod2 = linregress(self._x1, self._x2)
            resid2 = self._x2 - (mod2.slope * self._x1 + mod2.intercept)
            
            e_list = [resid1, resid2]
        
        test_result = {'test1': [], 'test2': [], 'test3': []}

        for e in e_list:
            test_result['test1'].append(ScmSelector._ks_test(e, alpha))
            test_result['test2'].append(ScmSelector._dp_test(e, alpha))
            if len(self._x1) < 4000:
                test_result['test3'].append(ScmSelector._sw_test(e, alpha))
            else: test_result['test3'].append(ScmSelector._anderson_test(e, alpha))
        
        vote_list = []
        for i in range(len(e_list)):
            vote = np.sum([test_result[key][i] for key in test_result])
            vote_list.append(vote)
        
        if len(vote_list)==1:
            self._test_result = 'non-gaussian' if np.sum(vote_list) >= int(vote_thres[voting_strategy]) else 'gaussian'
        else:
            self._test_result = 'non-gaussian' if all(np.sum(v) >= int(vote_thres[voting_strategy]) for v in vote_list) else 'gaussian'
        
        self._is_fitted = True
        
        self._selected_scm = Esa2Scm(self._x1, self._x2, self._prior_knowledge) if self._test_result == 'gaussian' else GradientNonGaussianScm(self._x1, self._x2, self._prior_knowledge)
        
        return self
    

    @property
    def selected_scm(self):
        if not self._is_fitted:
            raise RuntimeError("You must fit the ScmSelector first")
        
        print(f"{self._selected_scm.__class__.__name__}(x1={self._x1}, x2={self._x2}, prior_knowledge={self._prior_knowledge})")
        
        return self._selected_scm