"""

scmopy: Distribution-Agnostic Structural Causal Models Optimization in Python

The scmopy package is a composite package for causal discovery/analysis using several novel types of SCM Optimization algorithms.
The package also incorporates Distribution-Agnostic methods for causal estimation, which enables deviations from the necessity of any specific distributional assumption.

Should you use the scmopy package, please cite the following articles.
- Lee, Sanghoon (2024). ESA-2SCM for Causal Discovery: Causal Modeling with Elastic Segmentation-based Synthetic Instrumental Variable, SnB Political and Economic Research Institute, 1, 21. <snbperi.org/article/230>.
- S.Shimizu and Y.Kano (2008). Use of non-normality in structural equation modeling: Application to direction of causation, Journal of Statistical Planning and Inference, 138, 11, 3483-3491.

"""


from setuptools import setup, find_packages

with open("README.md", "r", encoding='utf-8') as fh:
    README = fh.read()

setup(
    author="Sanghoon Lee (DSsoli)",
    author_email="solisoli3197@gmail.com",
    name="scmopy",
    version="0.1.4",
    description="scmopy: Distribution-Agnostic Structural Causal Models Optimization in Python",
    long_description=README,
    long_description_content_type="text/markdown",
    install_requires=["numpy", "pandas", "scipy"],
    url="https://github.com/DSsoli/scmopy.git",
    packages=find_packages(include=['scmopy', 'scmopy.*']),
    package_data={"scmopy": ['LICENSE', 'examples/*']},
    include_package_data=True
)