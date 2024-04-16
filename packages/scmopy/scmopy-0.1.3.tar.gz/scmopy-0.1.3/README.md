# **scmopy**: Distribution-Agnostic Structural Causal Models Optimization in Python

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/DSsoli/scmopy/blob/main/LICENSE)
[![PyPI - Version](https://img.shields.io/pypi/v/scmopy.svg)](https://pypi.org/project/scmopy/)


scmopy is a composite package for causal discovery/analysis using several **novel** types of Structural Causal Models Optimization algorithms.
<br>

scmopy provides **Distribution-Agnostic** methods in identifying causality; in other words, users can deviate from the necessity of satisfying any specific distributional assumptions as regards to the dataset, and as regards to the whole process of causal estimation to hypothesis-testing.
<br>

The package is mainly structured in three parts:

1. **ESA-2SCM (Elastic Segment Allocation-based Two-Stage Least Squares SCM)**
- ESA-2SCM is a new method for detecting causality based on the Elastic Segment Allocation-based synthetic instrumental variables with 2SLS application for estimating structural causal models. 
- For details and documentation, please refer to my original article: <br>
- [Lee, Sanghoon (2024). **ESA-2SCM for Causal Discovery: Causal Modeling with Elastic Segmentation-based Synthetic Instrumental Variable**, *SnB Political and Economic Research Institute,* *1,* 21. <snbperi.org/article/230>](http://www.snbperi.org/article/230)
<br><br>

2. **Gradient Non-Gaussian SCM**
- Gradient Non-Gaussian SCM incorporates the information of higher order moment structures assuming non-gaussianity to determine the true causal direction.
- Gradient Non-Gaussian SCM is a customized implementation of S.Shimizu and Y.Kano's conceptualization of nnSEM. Specifically, the quadratic objective function based on the difference between the sample moments and theoretical moments is optimized via gradient method (defaulting to BFGS) instead of performing GLS.
- For details regarding the concepts of the original nnSEM, please refer to:
- S.Shimizu and Y.Kano (2008). **Use of non-normality in structural equation modeling: Application to direction of causation**, *Journal of Statistical Planning and Inference,* *138*, *11*, 3483-3491.
<br><br>

3. **Auto-SCM Selector for Optimization**
- The SCM Selector automatically determines the optimal model via pre-inspecting the dataset. 
- Internally, it utilizes voting methods in combination with multiple hypothesis testing techniques on the data's original distribution for the precision of model determination: ESA-2SCM is selected as the basemodel if the pre-inspection result suggests gaussianity, otherwise the Gradient Non-Gaussian SCM is selected.

For further details on each model's algorithm, refer to the **Models Overview** section below.

## Requirements

* Python3

* numpy

* pandas

* scipy

## Installation

To install the scmopy package, use `pip` as follows:

```sh
pip install scmopy
```

## Example Usage

```python
from scmopy.nongaussian_scm import GradientNonGaussianScm
from scmopy.gaussian_scm import Esa2Scm
from scmopy.model_selection import ScmSelector

import numpy as np # to generate sample data for demonstration
```

> Gradient Non-Gaussian SCM

```python
# Generate sample data for demonstration
N = 10000
np.random.seed(11)
x2 = np.random.gamma(shape=0.5, scale=0.5, size=N) # non-gaussian sample
noise = np.random.random(size=N) # non-gaussian noise
b12 = 1.8 # True Causal Coefficient set as 1.8
x1 = b12 * x2 + noise # True Causal Direction set as x2 -> x1

# Initialize GradientNonGaussianSCM with no prior knowledge on the causal direction
scm = GradientNonGaussianScm(x1, x2, prior_knowledge=None, unit_var=False)

# Fit the model
scm.fit(alpha=0.1) # Set alpha for chi2 test using the test statistic T2 for determination of causal direction

# To confirm the estimated True Causal Direction
print(scm.causal_direction)

# To confirm the estimated True Causal Coefficient
print(scm.causal_coef)

# To confirm the test statistic (T2) and p-value for hypothesis testing on the Causal Direction
print(scm.test_statistic)
print(scm.p_value)

# To confirm the fit score
print(scm.score)
```

```python
# For result summary:
scm.summary()
```

|                    | x2->x1             | x1->x2             |
|:-------------------|:-------------------|:-------------------|
| Causal Direction   | Decisive True      | Decisive False     |
| Causal Coefficient | 1.8010473505277451 | 0.3574865003509795 |
| Test Statistic     | 3.4739238216348447 | 646.2378958215542  |
| P-value            | 0.6273369079064182 | 0.0                |
| Reject H0          | False              | True               |
| Goodness of Fit    | 0.82038            | -                  |

<br><br>

> ESA-2SCM
```python
# Initialize ESA-2SCM with no prior knowledge on the causal direction
scm = Esa2Scm(x1, x2, prior_knowledge=None)

# Fit the model, using Synthetic IV generation method(syniv_method, default='esa') to estimate causality
# Adjust the parameter M(default=2) to manually manage the degree of correlation between the Synthetic IVs (2SLS-converted) and the respective endogenous variables
scm.fit(syniv_method="esa", M=3)

# To confirm the estimated True Causal Direction
print(scm.causal_direction)

# To confirm the estimated True Causal Coefficient
print(scm.causal_coef)

# To check the degree of correlation between the generated Synthetic IVs and the endogenous variables (x1 and x2, respectively):
print(scm.corr_x1_to_slsiv)
print(scm.corr_x2_to_slsiv)

# To confirm the true goodness of fit of the ESA-2SCM for determination of the causal direction:
print(scm.esa2scm_score)

# With causal direction determined via ESA-2SCM, to confirm the posthoc goodness of fit of the Regression Model using original variables:
print(scm.posthoc_score)
```

```python
# For result summary:
scm.summary()
```
|                             | x2->x1   | x1->x2    |
|-----------------------------|----------|-----------|
| Causal Direction            | True     | False     |
| Causal Coefficient          | 1.804851 | 0.385192  |
| Goodness of Fit             | 0.39664  | 0.35318   |
| Corr (2SLS_IV-Explanatory)  | 0.694676 | 0.774985  |
| Posthoc Goodness of Fit     | 0.82038  | -         |

<br><br>

> Auto SCM Selector for Optimal SCM Selection

```python
# Initialize Auto SCM Selector
selector = ScmSelector(x1, x2)

# Fit the selector
selector.fit(alpha=0.15, voting_strategy='strict')

# Confirm optimal model for the given dataset x1 and x2.
best_scm = selector.selected_scm

# Fit using the selected model
best_scm.fit()

# Confirm the estimated True Causal Direction
print(best_scm.causal_direction)

# Confirm the estimated True Causal Coefficient
print(best_scm.causal_coef)
```

```python
# For result summary:
best_scm.summary()
```
|                    | x2->x1             | x1->x2             |
|:-------------------|:-------------------|:-------------------|
| Causal Direction   | Decisive True      | Decisive False     |
| Causal Coefficient | 1.8010473505277451 | 0.3574865003509795 |
| Test Statistic     | 3.4739238216348447 | 646.2378958215542  |
| P-value            | 0.6273369079064182 | 0.0                |
| Reject H0          | False              | True               |
| Goodness of Fit    | 0.82038            | -                  |


## Models Overview

Gradient Non-Gaussian SCM accounts for the case where the exogenous variable or the noise follows non-gaussian distribution. <br>
ESA-2SCM, on the other hand, accounts for the case where the noise follows gaussian distribution.

In scmopy, these two models are deployed in a complementary manner, ultimately enabling Distribution-Agnostic SCM optimization for causal discovery.

> Gradient Non-Gaussian SCM

Gradient Non-Gaussian SCM is a customized implementation of S.Shimizu and Y.Kano's conceptualization of nnSEM (2008). More specifically: 
- the quadratic objective function based on the difference between the sample moments and theoretical moments is optimized via gradient method (defaulting to BFGS) instead of performing GLS. 
- Weight matrix is defined as $\hat{\Sigma}$ and Pseudo-inverse matrix $\hat{\Sigma}^+$ is used instead if the inverse matrix of $\hat{\Sigma}$ cannot be obtained.

<br>

With $\xi$ and $\eta$ defined as exogenous and endogenous vectors in observable $x$ and latent $f$, the standard SEM is denoted as:

<p align="center">
  <img src="https://github.com/DSsoli/scmopy/blob/main/img/1.png?raw=true" width="250"/>
</p>

Reduced form of the above with respect to $x$ can be rewritten as follows, with $G$ as the selection matrix which selects only the observed variables:

<p align="center">
  <img src="https://github.com/DSsoli/scmopy/blob/main/img/2.png?raw=true" width="110"/>
</p>

With $H_i$ as the selection matrix which selects non-duplicated elements, the first and second to fourth order moment structures of the SEM can be denoted, respectively, as (S.Shimizu and Y.Kano, 2008):

<p align="center">
  <img src="https://github.com/DSsoli/scmopy/blob/main/img/3.png?raw=true" width="140"/>
</p>

<p align="center">
  <img src="https://github.com/DSsoli/scmopy/blob/main/img/4.png?raw=true" width="500"/>
</p>

Assumption that the SEM is identifiable using moment structures is equivalent of:

<p align="center">
  <img src="https://github.com/DSsoli/scmopy/blob/main/img/5.png?raw=true" width="350"/>
</p>

Denote sample counterparts to the first and second to fourth theoretical moment structures above as:

<p align="center">
  <img src="https://github.com/DSsoli/scmopy/blob/main/img/6.png?raw=true" width="180"/>
</p>

<p align="center">
  <img src="https://github.com/DSsoli/scmopy/blob/main/img/7.png?raw=true" width="500"/>
</p>

Then with $\tau_0$ as the true parameter, the following holds:

<p align="center">
  <img src="https://github.com/DSsoli/scmopy/blob/main/img/8.png?raw=true" width="350"/>
</p>

With $m$ and $\sigma(\tau)$ denoted as:

<p align="center">
  <img src="https://github.com/DSsoli/scmopy/blob/main/img/9.png?raw=true" width="300"/>
</p>

$\tau$ can be estimated with:

<p align="center">
  <img src="https://github.com/DSsoli/scmopy/blob/main/img/10.png?raw=true" width="400"/>
</p>

S.Shimizu and Y.Kano (2008) obtains $\hat{\tau}$ with GLS using $\hat{V}$ for $\hat{U}$.

Gradient Non-Gaussian SCM in scmopy adopts instead a gradient method (defaulting to BFGS) for solving the above with $\hat{\Sigma}$ defined as:

<p align="center">
  <img src="https://github.com/DSsoli/scmopy/blob/main/img/11.png?raw=true" width="500"/>
</p>

and with $\tau$ estimation rewritten as:

<p align="center">
  <img src="https://github.com/DSsoli/scmopy/blob/main/img/12.png?raw=true" width="400"/>
</p>

Assuming unit variance $(I)$ and single parameter/moment ( $\tau$, $\sigma(\tau)$ ) for simplification:

<p align="center">
  <img src="https://github.com/DSsoli/scmopy/blob/main/img/13.png?raw=true" width="400"/>
</p>

so that

<p align="center">
  <img src="https://github.com/DSsoli/scmopy/blob/main/img/14.png?raw=true" width="300"/>
</p>

Applying chain rule,

<p align="center">
  <img src="https://github.com/DSsoli/scmopy/blob/main/img/15.png?raw=true" width="300"/>
</p>

Then, the basic form of gradient descent can be written as:

<p align="center">
  <img src="https://github.com/DSsoli/scmopy/blob/main/img/16.png?raw=true" width="350"/>
</p>

Generalizing,

<p align="center">
  <img src="https://github.com/DSsoli/scmopy/blob/main/img/17.png?raw=true" width="350"/>
</p>

<p align="center">
  <img src="https://github.com/DSsoli/scmopy/blob/main/img/18.png?raw=true" width="350"/>
</p>

<p align="center">
  <img src="https://github.com/DSsoli/scmopy/blob/main/img/19.png?raw=true" width="350"/>
</p>

Pseudo-inverse matrix of $\hat{\Sigma}$ is used instead if the inverse matrix cannot be obtained.

Application as regards to the determination of true causal direction is identical to the case of nnSEM (S.Shimizu and Y.Kano, 2008), as follows.

Suppose that we are interested in identifying the true causal direction between the two random variables $x_1$ and $x_2$ ($x_1$ -> $x_2$ vs. $x_2$ -> $x_1$). Then the SCM for testing can be denoted as (after mean-centering):

<p align="center">
  <img src="https://github.com/DSsoli/scmopy/blob/main/img/20.png?raw=true" width="200"/>
</p>

with,

<p align="center">
  <img src="https://github.com/DSsoli/scmopy/blob/main/img/21.png?raw=true" width="350"/>
</p>

The first- and second-order moment structures of $(1)$ can be obtained as:

<p align="center">
  <img src="https://github.com/DSsoli/scmopy/blob/main/img/22.png?raw=true" width="350"/>
</p>

<p align="center">
  <img src="https://github.com/DSsoli/scmopy/blob/main/img/23.png?raw=true" width="450"/>
</p>

<p align="center">
  <img src="https://github.com/DSsoli/scmopy/blob/main/img/24.png?raw=true" width="450"/>
</p>

As there are as many parameters as the sample moments, models $(1)$ and $(2)$ are saturated, and equivalent (as they provide the same moment structures thus disabling to determine which model is better based on these test statistics alone) to each other when using only up to second order moments.

Now, expanding up to third and fourth order moment structures, S.Shimizu and Y.Kano (2008) prove that under the satisfaction of the following three conditions:<br>
(1) Either the exogenous variable $x_2$ or the noise $e_1$ is non-gaussian (when assuming that the model $(1)$ holds True) <br>
(2) $corr(x_1, x_2) \neq 0$ <br>
(3) $-1 < corr(x_1, x_2) < 1$ <br>
models $(1)$ and $(2)$ can be differentiated. 

That is to say, <br>
with $r = corr(x_1,x_2)$, and $i$-th order moment structure defined as:

<p align="center">
  <img src="https://github.com/DSsoli/scmopy/blob/main/img/25.png?raw=true" width="190"/>
</p>

and,

<p align="center">
  <img src="https://github.com/DSsoli/scmopy/blob/main/img/26.png?raw=true" width="300"/>
</p>

to get the isolated quantity from the fourth order moment ( $E(z^4)$ ), especially the parts that are independent from the lower order moments, leaving a quantity that captures the "pure" fourth-order behavior of the distribution,

if (1) $0< |r| < 1$ and (2) either $E(x_2^3), E(e_1^3), cum_4(x_2)$, or $cum_4(e_1)$ is non-zero, the following holds:

<p align="center">
  <img src="https://github.com/DSsoli/scmopy/blob/main/img/27.png?raw=true" width="350"/>
</p>

so that the models $(1)$ and $(2)$ are distinguishable using the moments up to third or fourth moment orders.

More specifically,

<p align="center">
  <img src="https://github.com/DSsoli/scmopy/blob/main/img/28.png?raw=true" width="330"/>
</p>

<p align="center">
  <img src="https://github.com/DSsoli/scmopy/blob/main/img/29.png?raw=true" width="180"/>
</p>

For 

<p align="center">
  <img src="https://github.com/DSsoli/scmopy/blob/main/img/30.png?raw=true" width="150"/>
</p>

to hold,

<p align="center">
  <img src="https://github.com/DSsoli/scmopy/blob/main/img/31.png?raw=true" width="350"/>
</p>

should hold. Solving for the matrix,

<p align="center">
  <img src="https://github.com/DSsoli/scmopy/blob/main/img/32.png?raw=true" width="400"/>
</p>

<p align="center">
  <img src="https://github.com/DSsoli/scmopy/blob/main/img/33.png?raw=true" width="400"/>
</p>

Similar derivation process can be applied for the fourth-order moment.

Thus, the two models $(1)$ and $(2)$ are distinguishable from each other using either third- and/or fourth-order moments, with each order moment structure ( e.g., for model $(1)$ ) defined respectively as:

<p align="center">
  <img src="https://github.com/DSsoli/scmopy/blob/main/img/34.png?raw=true" width="500"/>
</p>

<p align="center">
  <img src="https://github.com/DSsoli/scmopy/blob/main/img/35.png?raw=true" width="500"/>
</p>

and with $H_0$ and $H_1$ defined as:

<p align="center">
  <img src="https://github.com/DSsoli/scmopy/blob/main/img/36.png?raw=true" width="180"/>
</p>

Test statistic $T_2$ to test $H_0$ is defined as (S.Shimizu and Y.Kano, 2008):

<p align="center">
  <img src="https://github.com/DSsoli/scmopy/blob/main/img/37.png?raw=true" width="180"/>
</p>

<p align="center">
  <img src="https://github.com/DSsoli/scmopy/blob/main/img/38.png?raw=true" width="350"/>
</p>

or, in case of Gradient Non-Gaussian SCM in scmopy,

<p align="center">
  <img src="https://github.com/DSsoli/scmopy/blob/main/img/39.png?raw=true" width="350"/>
</p>

where $T_2$ asymptotically follows chi-squared distribution with dof $u-v$ where $u$ is the total number of distinct moments employed and  $v$ is the total number of parameters estimated.

Reference and the original conceptualization of nnSEM by S.Shimizu and Y.Kano (2008):
- S.Shimizu and Y.Kano (2008). **Use of non-normality in structural equation modeling: Application to direction
of causation**, *Journal of Statistical Planning and Inference,* *138*, *11*, 3483-3491.

<br><br>

> ESA-2SCM

ESA-2SCM is a new method for detecting causality based on Elastic Segment Allocation-based synthetic instrumental variables with 2SLS application for estimating structural causal models.

Suppose that you are interested in discovering the causal relationship between $x_1$ and $x_2$ (e.g., determining the *true causal direction*: $x_1$ -> $x_2$ vs. $x_2$ -> $x_1$, measuring the magnitude of *causal impact*):
<p align="center">
  <img src="https://github.com/DSsoli/scmopy/blob/main/img/40.png?raw=true", width="200"/>
</p>

Estimation of the above equation under standard OLS is *structurally* biased and inconsistent due to endogeneity:
<p align="center">
  <img src="https://github.com/DSsoli/scmopy/blob/main/img/41.png?raw=true" width="350"/>
</p>

where
<p align="center">
  <img src="https://github.com/DSsoli/scmopy/blob/main/img/42.png?raw=true" width="300"/>
</p>

thus,
<p align="center">
  <img src="https://github.com/DSsoli/scmopy/blob/main/img/43.png?raw=true" width="500"/>
</p>


The estimators are also asymptotically inconsistent, as:
<p align="center">
  <img src="https://github.com/DSsoli/scmopy/blob/main/img/44.png?raw=true" width="310"/>
</p>


**ESA-2SCM** provides a countermeasure to such problem, enabling the determination of true *causal direction* and estimation of the true *causal coefficient* through the following procedures.
1. Vector definition:
<p align="center">
  <img src="https://github.com/DSsoli/scmopy/blob/main/img/45.png?raw=true" width="450"/>
</p>

2. Sorting:
<p align="center">
  <img src="https://github.com/DSsoli/scmopy/blob/main/img/46.png?raw=true" width="500"/>
</p>

3. Set initial number of segments *(M)*:
<p align="center">
  <img src="https://github.com/DSsoli/scmopy/blob/main/img/47.png?raw=true" width="500"/>
</p>

4. Segment size allocation:
<p align="center">
  <img src="https://github.com/DSsoli/scmopy/blob/main/img/48.png?raw=true" width="460"/>
</p>

5. Elastic adjustment algorithm for adjusting the number of segments:
<p align="center">
  <img src="https://github.com/DSsoli/scmopy/blob/main/img/49.png?raw=true" width="580"/>
</p>

6. Grouping based on the adjusted sizes and number of segments:
<p align="center">
  <img src="https://github.com/DSsoli/scmopy/blob/main/img/50.png?raw=true" width="450"/>
</p>

7. Segment value assignment:
<p align="center">
  <img src="https://github.com/DSsoli/scmopy/blob/main/img/51.png?raw=true" width="420"/>
</p>

8. Apply 2SLS using the generated Synthetic IV vectors *(Z)*: <br>

    * Get $z_1$ and  $z_2$ via applying the process (1) to (7) for  $x_1$ and  $x_2$, then perform 2SLS to estimate for:
 
<p align="center">
  <img src="https://github.com/DSsoli/scmopy/blob/main/img/53.png?raw=true" width="200"/>
</p>  

Compare fits to determine the true causal direction, and estimate the true causal coefficient from the correctly identified model.

<br>

Reference and detailed documentation for the ESA-2SCM algorithm:
* Lee, Sanghoon (2024). **ESA-2SCM for Causal Discovery: Causal Modeling with Elastic Segmentation-based Synthetic Instrumental Variable**, *SnB Political and Economic Research Institute,* *1,* 21. <snbperi.org/article/230> [[ARTICLE LINK]](http://www.snbperi.org/article/230)

## Examples
Examples of running scmopy in Jupyter Notebook are included in [scmopy/examples](https://github.com/DSsoli/scmopy/tree/main/examples)

## License
scmopy package is licensed under the terms of the [MIT license](https://github.com/DSsoli/scmopy/blob/main/LICENSE)

## References

### scmopy Package

Should you use the scmopy package to perform causal discovery, please cite my original article and the original article by S.Shimizu and Y.Kano:

* Lee, Sanghoon (2024). **ESA-2SCM for Causal Discovery: Causal Modeling with Elastic Segmentation-based Synthetic Instrumental Variable**, *SnB Political and Economic Research Institute,* *1,* 21. <snbperi.org/article/230> [[ARTICLE LINK]](http://www.snbperi.org/article/230)

* S.Shimizu and Y.Kano (2008). **Use of non-normality in structural equation modeling: Application to direction of causation**, *Journal of Statistical Planning and Inference,* *138*, *11*, 3483-3491.