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
import scipy as sp
import logging
from .components import r2_score
from .base import BaseCM


class GradientNonGaussianScm(BaseCM):
    
    def __init__(self, x1, x2, prior_knowledge=None, unit_var=False):
        super().__init__(x1, x2, prior_knowledge)
        
        self._N = len(self._x1)
        
        x1_mean_centered = self._x1 - np.mean(self._x1)
        x2_mean_centered = self._x2 - np.mean(self._x2)
        
        x1_mean_centered_unit_var = (self._x1 - np.mean(self._x1)) / np.std(self._x1)
        x2_mean_centered_unit_var = (self._x2 - np.mean(self._x2)) / np.std(self._x2)
        
        self._x1 = x1_mean_centered
        self._x2 = x2_mean_centered
        self._x1_rev = x2_mean_centered
        self._x2_rev = x1_mean_centered
        
        if unit_var:
            self._x1 = x1_mean_centered_unit_var
            self._x2 = x2_mean_centered_unit_var
            self._x1_rev = x2_mean_centered_unit_var
            self._x2_rev = x1_mean_centered_unit_var


    @staticmethod
    def _sample_order_moments(x1, x2):
        
        m10 = np.mean(x1)
        m1 = m10

        m20 = np.mean(x1**2 * x2**0)
        m11 = np.mean(x1**1 * x2**1)
        m02 = np.mean(x1**0 * x2**2)
        m2 = np.array([m20, m11, m02]).reshape(-1,1)

        m30 = np.mean(x1**3 * x2**0)
        m21 = np.mean(x1**2 * x2**1)
        m12 = np.mean(x1**1 * x2**2)
        m03 = np.mean(x1**0 * x2**3)
        m3 = np.array([m30, m21, m12, m03]).reshape(-1,1)

        m40 = np.mean(x1**4 * x2**0)
        m31 = np.mean(x1**3 * x2**1)
        m22 = np.mean(x1**2 * x2**2)
        m13 = np.mean(x1**1 * x2**3)
        m04 = np.mean(x1**0 * x2**4)
        m4 = np.array([m40, m31, m22, m13, m04]).reshape(-1,1)

        M = np.vstack([m1, m2, m3, m4])
        

        m10_dev = x1 - m10
        m20_dev = (x1**2 * x2**0) - m20
        m11_dev = (x1**1 * x2**1) - m11
        m02_dev = (x1**0 * x2**2) - m02
        m30_dev = (x1**3 * x2**0) - m30
        m21_dev = (x1**2 * x2**1) - m21
        m12_dev = (x1**1 * x2**2) - m12
        m03_dev = (x1**0 * x2**3) - m03
        m40_dev = (x1**4 * x2**0) - m40
        m31_dev = (x1**3 * x2**1) - m31
        m22_dev = (x1**2 * x2**2) - m22
        m13_dev = (x1**1 * x2**3) - m13
        m04_dev = (x1**0 * x2**4) - m04

        M_deviation_matrix = np.column_stack([
            m10_dev, 
            m20_dev, m11_dev, m02_dev, 
            m30_dev, m21_dev, m12_dev, m03_dev,
            m40_dev, m31_dev, m22_dev, m13_dev, m04_dev
        ])
        
        return M, M_deviation_matrix
    
    
    @staticmethod
    def _calc_sigma_inv(deviation_matrix):
        
        Sigma = np.cov(deviation_matrix, rowvar=False)
        
        try:
            Sigma_inv = np.linalg.inv(Sigma)
            
        except np.linalg.LinAlgError:
            logging.warning(f"moment structure Sigma matrix is singular. using pseudo-inverse instead.")
            Sigma_inv = np.linalg.pinv(Sigma)
            
        return Sigma_inv


    @staticmethod
    def _argmin_quadratic_objective(tau, M, Sigma_inv):
        
        Ex2_opt, Ex2_squared_opt, Ee1_squared_opt, Ex2_cubed_opt, Ee1_cubed_opt, \
        Ex2_fourth_opt, Ee1_fourth_opt, b12_opt = tau
        
        H1 = b12_opt
        E1 = Ex2_opt
        sigma1_tau1_val = H1 * E1
        
        H2 = np.array([
            [b12_opt**2, 1],
            [b12_opt, 0],
            [1, 0]
        ])
        E2 = np.array([
            [Ex2_squared_opt],
            [Ee1_squared_opt]
        ])
        sigma2_tau2_val = H2 @ E2
        
        H3 = np.array([
            [b12_opt**3, 1],
            [b12_opt**2, 0],
            [b12_opt, 0],
            [1, 0]
        ])
        E3 = np.array([
            [Ex2_cubed_opt],
            [Ee1_cubed_opt]
        ])
        sigma3_tau3_val = H3 @ E3
        
        H4 = np.array([
            [b12_opt**4, 6*(b12_opt**2), 1],
            [b12_opt**3, 3*(b12_opt), 0],
            [b12_opt**2, 1, 0],
            [b12_opt, 0, 0],
            [1, 0, 0]
        ])
        E4 = np.array([
            [Ex2_fourth_opt],
            [Ex2_squared_opt * Ee1_squared_opt],
            [Ee1_fourth_opt]
        ])
        sigma4_tau4_val = H4 @ E4
        
        sigma_tau_val = np.vstack([sigma1_tau1_val, sigma2_tau2_val, sigma3_tau3_val, sigma4_tau4_val])
        
        diff = M - sigma_tau_val
        
        return (diff.T @ Sigma_inv @ diff)[0][0]

    
    @staticmethod
    def _init_tau(x1, x2):
        
        res = sp.stats.linregress(x=x2, y=x1)
        e1 = x1 - res.slope * x2 # assume intercept as 0, as per the model specification, and as per x1 and x2 are mean_centered
        # res = sm.OLS(x1, x2).fit()
        # e1 = res.resid
        
        Ex2 = np.mean(x2)
        Ex2_squared = np.mean(x2**2)
        Ee1_squared = np.mean(e1**2)
        Ex2_cubed = np.mean(x2**3)
        Ee1_cubed = np.mean(e1**3)
        Ex2_fourth = np.mean(x2**4)
        Ee1_fourth = np.mean(e1**4)
        b12 = res.slope
        # b12 = res.params[0]
        
        tau_init = [Ex2, Ex2_squared, Ee1_squared, Ex2_cubed, Ee1_cubed, Ex2_fourth, Ee1_fourth, b12]
        
        return tau_init
    
    
    @staticmethod
    def _fit(x1, x2, N):
        
        M, M_deviation_matrix = GradientNonGaussianScm._sample_order_moments(x1, x2)
        Sigma_inv = GradientNonGaussianScm._calc_sigma_inv(M_deviation_matrix)
        tau_init = GradientNonGaussianScm._init_tau(x1, x2)
        
        result = sp.optimize.minimize(GradientNonGaussianScm._argmin_quadratic_objective, tau_init, args=(M, Sigma_inv), method='BFGS')
        
        tau_hat = result.x
        tau_idx = ['Ex2_opt', 'Ex2_squared_opt', 'Ee1_squared_opt', 'Ex2_cubed_opt', \
            'Ee1_cubed_opt', 'Ex2_fourth_opt', 'Ee1_fourth_opt', 'b12_opt']
        tau_hat = dict(zip(tau_idx, tau_hat))

        H1_hat = tau_hat['b12_opt']
        E1_hat = tau_hat['Ex2_opt']
        sigma1_tau1_hat = H1_hat * E1_hat

        H2_hat = np.array([
            [tau_hat['b12_opt']**2, 1],
            [tau_hat['b12_opt'], 0],
            [1, 0]
        ])
        E2_hat = np.array([
            [tau_hat['Ex2_squared_opt']],
            [tau_hat['Ee1_squared_opt']]
        ])
        sigma2_tau2_hat = H2_hat @ E2_hat

        H3_hat = np.array([
            [tau_hat['b12_opt']**3, 1],
            [tau_hat['b12_opt']**2, 0],
            [tau_hat['b12_opt'], 0],
            [1, 0]
        ])
        E3_hat = np.array([
            [tau_hat['Ex2_cubed_opt']],
            [tau_hat['Ee1_cubed_opt']]
        ])
        sigma3_tau3_hat = H3_hat @ E3_hat

        H4_hat = np.array([
            [tau_hat['b12_opt']**4, 6*(tau_hat['b12_opt']**2), 1],
            [tau_hat['b12_opt']**3, 3*(tau_hat['b12_opt']), 0],
            [tau_hat['b12_opt']**2, 1, 0],
            [tau_hat['b12_opt'], 0, 0],
            [1, 0, 0]
        ])
        E4_hat = np.array([
            [tau_hat['Ex2_fourth_opt']],
            [tau_hat['Ex2_squared_opt'] * tau_hat['Ee1_squared_opt']],
            [tau_hat['Ee1_fourth_opt']]
        ])
        sigma4_tau4_hat = H4_hat @ E4_hat

        sigma_tau_hat = np.vstack([sigma1_tau1_hat, sigma2_tau2_hat, sigma3_tau3_hat, sigma4_tau4_hat])

        diff_hat = M - sigma_tau_hat
        F_tau_hat = (diff_hat.T @ Sigma_inv @ diff_hat)[0][0]

        T1 = N * F_tau_hat
        T2 = T1 / (1 + F_tau_hat)
        
        return tau_hat['b12_opt'], T2
    
    
    def fit(self, alpha=0.10):
        
        if self._prior_knowledge is not None:
            if self._prior_knowledge == 'x2->x1':
                self._b, self._T2 = GradientNonGaussianScm._fit(self._x1, self._x2, self._N)
                pred = self._b * self._x2
                self._score = round(r2_score(self._x1, pred), 5) 
                
            else: 
                self._b, self._T2 = GradientNonGaussianScm._fit(self._x1_rev, self._x2_rev, self._N)
                pred = self._b * self._x2_rev
                self._score = round(r2_score(self._x1_rev, pred), 5)
            
            self._causal_dir = self._prior_knowledge
            self._confidence = 'Decisive'
            
            self._true_causal_coef = self._b
            self._true_test_statistic = self._T2
            dof = 5
            self._true_p_value = 1 - sp.stats.chi2.cdf(self._T2, dof)
            
        else:
            self._b12, self._T2 = GradientNonGaussianScm._fit(self._x1, self._x2, self._N)
            self._b21, self._T2_rev = GradientNonGaussianScm._fit(self._x1_rev, self._x2_rev, self._N)
            
            dof = 5 # number of distinct moments employed (13) - number of parameters estimated (8)
            critical_value = sp.stats.chi2.ppf(1 - alpha, dof)
            
            self._reject_H0 = self._T2 > critical_value
            self._reject_H0_rev = self._T2_rev > critical_value
            
            self._p_value = 1 - sp.stats.chi2.cdf(self._T2, dof)
            self._p_value_rev = 1 - sp.stats.chi2.cdf(self._T2_rev, dof)
            
            self._confidence = 'Decisive' if self._reject_H0 != self._reject_H0_rev else 'Weak'
            self._causal_dir = 'x2->x1' if self._T2_rev > self._T2 else 'x1->x2' if self._T2_rev < self._T2 else 'undetermined'
            
            self._true_causal_coef = self._b12 if self._causal_dir == 'x2->x1' else self._b21 if self._causal_dir == 'x1->x2' else 'undetermined'
            self._true_test_statistic = self._T2 if self._causal_dir == 'x2->x1' else self._T2_rev if self._causal_dir == 'x1->x2' else 'undetermined'
            self._true_p_value = self._p_value if self._causal_dir == 'x2->x1' else self._p_value_rev if self._causal_dir == 'x1->x2' else 'undetermined'
            
            self._score = round(r2_score(self._x1, self._b12 * self._x2), 5) if self._causal_dir == 'x2->x1' \
                else round(r2_score(self._x1_rev, self._b21 * self._x2_rev), 5) if self._causal_dir == 'x1->x2' else 'undetermined'
                
        return self

    
    def _summary(self):
        
        summary_idx = ['Causal Direction', "Causal Coefficient",  'Test Statistic', 'P-value', "Reject H0", "Goodness of Fit"]
        
        if self._prior_knowledge is not None:
            self._result = pd.DataFrame({self._prior_knowledge + " (Predetermined)": [self._prior_knowledge, self._b, self._score]}, index=[summary_idx[0], summary_idx[1], summary_idx[-1]])
            
        else:
            summary_columns = ['x2->x1', 'x1->x2']
            summary_values = [self._confidence + ' ' + str(self._causal_dir == 'x2->x1'), self._b12, self._T2, self._p_value, self._reject_H0]
            summary_values_rev = [self._confidence + ' ' + str(self._causal_dir == 'x1->x2'), self._b21, self._T2_rev, self._p_value_rev, 
                                    self._reject_H0_rev]
            
            _result = pd.DataFrame({summary_columns[0]:summary_values, summary_columns[1]:summary_values_rev}, 
                                        index=summary_idx[:-1])
            
            score_df = pd.DataFrame({summary_columns[0]: [self._score if self._causal_dir==summary_columns[0] else '-'], 
                                     summary_columns[1]: [self._score if self._causal_dir==summary_columns[1] else '-']
                                     }, index=[summary_idx[-1]])
            self._result = pd.concat([_result, score_df])
            
        return self._result
        

    @property
    def x1_preprocessed(self):
        return self._x1
    
    @property
    def x2_preprocessed(self):
        return self._x2
    
    @property
    def causal_coef(self):
        return self._true_causal_coef
    
    @property
    def test_statistic(self):
        return self._true_test_statistic
    
    @property
    def p_value(self):
        return self._true_p_value

    @property
    def causal_direction(self):
        return self._causal_dir
    
    @property
    def confidence(self):
        return self._confidence
    
    @property
    def score(self):
        return self._score
    
    @property
    def summary(self):
        return self._summary

    @property
    def b(self):
        """
        Causal Impact Coef. of the prior knowledge model
        """
        if hasattr(self, '_b'):
            return self._b
        raise AttributeError("Prior Knowledge has not been set.")
    
    @property
    def b12(self):
        """
        Causal Impact Coef. of x2 -> x1
        """
        
        if hasattr(self, '_b12'):
            return self._b12
        raise AttributeError("Prior knowledge has been set.")
    
    @property
    def b21(self):
        """
        Causal Impact Coef. of x1 -> x2
        """
        if hasattr(self, '_b21'):
            return self._b21
        raise AttributeError("Prior knowledge has been set.")
    
    @property
    def T2(self):
        """
        Test Statistic for x2 -> x1,
        or in case of prior knowledge,
        Test Statistic for the direction of such knowledge
        """
        return self._T2
    
    @property
    def T2_rev(self):
        """
        Test Statistic for x1 -> x2
        """
        if hasattr(self, '_T2_rev'):
            return self._T2_rev
        raise AttributeError("Prior knowledge has been set.") 

    
