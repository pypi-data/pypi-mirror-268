"""

scmopy: Distribution-Agnostic Structural Causal Models Optimization in Python

The scmopy package is a composite package for causal discovery/analysis using several novel types of SCM Optimization algorithms.
The package also incorporates Distribution-Agnostic methods for causal estimation, which enables deviations from the necessity of any specific distributional assumption.

Should you use the scmopy package, please cite the following articles.
- Lee, Sanghoon (2024). ESA-2SCM for Causal Discovery: Causal Modeling with Elastic Segmentation-based Synthetic Instrumental Variable, SnB Political and Economic Research Institute, 1, 21. <snbperi.org/article/230>.
- S.Shimizu and Y.Kano (2008). Use of non-normality in structural equation modeling: Application to direction of causation, Journal of Statistical Planning and Inference, 138, 11, 3483-3491.

"""


import numpy as np
import scipy.stats as ss
import warnings


class SynIV:
    
    _warning_status = False
    
    @staticmethod
    def dense_rank(x):
        z = ss.rankdata(x, method="dense")
        if len(np.unique(z))==1:
            warnings.warn("0 variance for given sample", UserWarning)
            SynIV._warning_status = True
        
        return z
    
    
    @staticmethod
    def esa(x, M=2):
        n = len(x)
        idx_sorted = np.argsort(x)
        original_M = M
                
        if M < 2: raise ValueError("Minimum number of segments (M) must be a positive integer greater than or equal to 2")

        def check_concentration(M):
            unique_elements, counts = np.unique(x, return_counts=True)
            max_concentration_threshold = 1 / M
            max_concentration = np.max(counts) / n
            return max_concentration, max_concentration_threshold, max_concentration <= max_concentration_threshold
        
        fixed_thres = 1/M
        while M >= 2:
            max_concent, max_concent_threshold, threshold_check = check_concentration(M)
            if threshold_check:
                break
            M -= 1
        
        if M < 2:
            warnings.warn(f"""
                            Data is excessively concentrated on a single segment to perform meaningful ESA. Using Dense Rank method instead.
                            (Single value accounts for {max_concent*100:.2f}% of the total dataset while single segment threshold for M={original_M} is fixed at {fixed_thres*100:.2f}%).
                            (This may indicate bias in the dataset, and may happen more commonly if the provided data is discrete and imbalanced). 
                            """, UserWarning)
            return SynIV.dense_rank(x)
        
        if M != original_M:
            warnings.warn(f"""
                            Data is excessively concentrated on a single segment to perform meaningful ESA. Using M={M} instead of M={original_M}.
                            (Single value accounts for {max_concent*100:.2f}% of the total dataset while single segment threshold for M={original_M} is fixed at {fixed_thres*100:.2f}%).
                            (This may indicate bias in the dataset, and may happen more commonly if the provided data is discrete and imbalanced). 
                            """, UserWarning)

        segment_sizes = [n // M + (1 if i < n % M else 0) for i in range(M)]
        boundaries = np.cumsum(segment_sizes)
        z = np.zeros(n, dtype=int)  
        
        start_idx = 0
        for assign_segment_value, boundary in enumerate(boundaries, start=1):
            segment_indices = idx_sorted[start_idx:boundary]
            z[segment_indices] = assign_segment_value
            start_idx = boundary
        
        return z
    
    
    @staticmethod
    def m_split(x, strategy: str = 'auto'):
        strategies = ['auto', 'median', 'mean']
        if strategy not in strategies: raise ValueError(f"Invalid strategy name '{strategy}'")
        
        mean_val, med_val = np.mean(x), np.median(x)
        
        def auto_strategy():
            if med_val != np.max(x):
                z = np.array([1 if i > med_val else -1 for i in x])
                if len(np.unique(z))==1:
                    z = np.array([1 if i > mean_val else -1 for i in x])
                    if len(np.unique(z))==1:
                        z = SynIV.dense_rank(x)
                        
            else: z = SynIV.dense_rank(x)
            return z
        
        def median_strategy():
            return np.array([1 if i > med_val else -1 for i in x])
        
        def mean_strategy():
            return np.array([1 if i > mean_val else -1 for i in x])
        
        strategy_funcs = {
            'auto': auto_strategy,
            'median': median_strategy,
            'mean': mean_strategy
        }
        
        z = strategy_funcs[strategy]()
        
        if len(np.unique(z))==1 and not SynIV._warning_status:
            warnings.warn("0 variance for given sample", UserWarning)
            SynIV._warning_status = True
            
        return z
    
    
    @staticmethod
    def get_syniv(method="esa"):
        syniv_map = {
            "esa": SynIV.esa,
            "dense_rank": SynIV.dense_rank,
            "m_split": SynIV.m_split
        }
        
        try:
            return syniv_map[method]
        except:
            raise ValueError(f"Invalid method name '{method}'")


def r2_score(y_true, y_pred):
    r2 = 1 - np.sum((y_true - y_pred)**2) / np.sum((y_true - np.mean(y_true))**2)
    return r2
