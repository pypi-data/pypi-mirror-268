# dualPredictor: An Open-Source Tool for Simultaneously Grade Prediction and At-Risk Student Classification

by Dong, Cheng, and Kan

## Introduction

The dualPredictor is a tool that combines regression analysis with binary classification to forecast student academic outcomes and identify at-risk students. This user guide provides a step-by-step walkthrough on how to install and use the dualPredictor package. The figure below illustrates the mechanism of how dualPredictor generates dual output (regression and classification) by combining a regressor and a metric.

![](https://github.com/098765d/dualPredictor/raw/eb30145140a93d355342340d2a7ab256ccbbbf6e/figs/how_dual_works.png)
**Fig 1**: Mechanism of how dualPredictor generates dual outputs.

## Motivation
The motivation behind the dualPredictor package is to make the use of complex models as simple as possible for all users, regardless of their coding experience. The model package is designed using the same syntax as the popular scikit-learn models, making it easy for users with experience in scikit-learn to quickly start using the dualPredictor. The model attributes, model methods(model.fit(X, y); model.predict(X)) are intentionally designed to mimic the scikit-learn model object, providing a familiar and user-friendly experience for user.
```python
# intialize the model, specify the parameters
model = DualModel(model_type='lasso', metric='f1_score', default_cut_off=2.5)
```
**Table 1**: Model methods and attributes (same style as sklearn model object)
| Model Methods | Description |
|--------------|-------------|
| `fit(X, y)`  | - **X**: The input training data, pandas data frame. <br> - **y**: The target values (predicted grade). <br> - **Returns**: Fitted DualModel instance |
| `predict(X)` | - **X**: The input training data, pandas' data frame. |

| Model Attributes   | Description                                                   |
|--------------------|---------------------------------------------------------------|
| `alpha_`           | The value of penalization in Lasso and ridge, for OLS alpha = 0 |
| `coef_`            | The coefficients of the model                                  |
| `Intercept_`       | The intercept value of the model                               |
| `feature_names_in_`| Names of features during model training                        |
| `optimal_cut_off`  | The optimal cut-off value that maximizes the metric            |

## Installation

You can install the dualPredictor package via PyPI or GitHub. Choose one of the following methods:

### PyPI Installation

```bash
pip install dualPredictor
```
### GitHub Installation (Recommended; Latest Version)
```bash
pip install git+https://github.com/098765d/dualPredictor.git
```

## Getting Started
**1. Import the Package:** Import the dualPredictor package in your Python environment.
```python
from dualPredictor import DualModel, model_plot
```
**2. Model Initialization:** 
Create a DualModel instance by specifying the regression model type ('lasso', 'ridge', or 'ols'), the metric for cutoff tuning ('f1_score', 'f2_score', or 'youden_index'), and a default cutoff value.
```python
model = DualModel(model_type='lasso', metric='youden_index', default_cut_off=2.5)
```
**3. Model Fitting:** Fit the model to your dataset using the fit method.
```python
model.fit(X_train, y_train)
```
- X: The input training data (pandas DataFrame).
- y: The target values (predicted grades).

**4. Predictions:** Use the prediction method to generate grade predictions and at-risk classifications.
  ```python
# example for demo only, model prediction dual output
y_train_pred,y_train_label_pred=model.predict(X_train)

# example of 1st model output = predicted scores (regression result)
y_train_pred
array([3.11893389, 3.06013236, 3.05418893, 3.09776197, 3.14898782,
       2.37679417, 2.99367804, 2.77202421, 2.9603209 , 3.01052573,
       2.99974477, 3.11286716, 3.14708887, 2.78737598, 2.88134869,
       3.07517748, 3.17370297, 3.26615469, 3.2328493 , 2.98423656,
       3.02108518, 2.87746064, 3.03491596, 2.89875586, 3.11079315,
       3.23177653, 3.34291929, 2.57402463, 3.27019917, 3.20073168,
       2.94514418, 3.25307175, 3.19145494, 3.15909904, 3.01481681,
       3.07551728, 2.70973767, 3.07226583, 3.04692613, 2.8883649 ,
       2.63833457, 3.03978663, 3.20974038, 3.13091091, 3.42223703,
       3.07012029, 3.01981077, 3.22368756, 2.69376153, 2.93594929,
       2.91493381, 3.22273808, 2.59310411, 3.00767959, 3.21869359,
       2.86065334, 3.16865551, 3.11258742, 2.87948289, 2.64564212,
       2.88646595, 3.48716006, 3.14482003, 3.15513751, 3.05299286,
       3.20858237, 2.63172024, 2.42824269, 2.88352738, 3.0479989 ,
       2.82405611, 3.16516577, 2.94324523, 3.4453079 , 2.48497569,
       3.00081754, 3.04180887, 3.32979373, 3.12686642, 2.90359338,
       2.95509896, 2.96429385, 3.44471154, 3.20251564, 3.08765075,
       2.5607482 , 3.23986551, 3.19644891, 3.16032825, 2.68092384,
       3.04907167, 2.8159268 , 3.05030088, 3.178372  ])

# example of 2nd model output = predicted at-risk status (binary label)
y_train_label_pred
array([0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0,
       0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0,
       1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0,
       0, 1, 0, 0, 0, 0])
```
- y_train_pred: Predicted grades (regression result).
- y_train_label_pred: Predicted at-risk status (binary label).

**5.Visualization:** Visualize the model's performance using the model_plot module (Optional)
```python
# Scatter plot for regression analysis
model_plot.plot_scatter(y_pred, y_true)

# Confusion matrix for binary classification
model_plot.plot_cm(y_label_true, y_label_pred)

# Feature importance plot
model_plot.plot_feature_coefficients(coef=model.coef_, feature_names=model.feature_names_in_)
```

## References

- Fluss, R., Faraggi, D., & Reiser, B. (2005). Estimation of the Youden Index and its associated cutoff point. _Biometrical Journal: Journal of Mathematical Methods in Biosciences_, 47(4), 458-472.
- Hoerl, A. E., & Kennard, R. W. (1970). Ridge regression: Biased estimation for nonorthogonal problems. _Technometrics_, 12(1), 55-67.
- Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., ... & Duchesnay, É. (2011). Scikit-learn: Machine learning in Python. _The Journal of Machine Learning Research_, 12, 2825-2830.
- Tibshirani, R. (1996). Regression shrinkage and selection via the lasso. _Journal of the Royal Statistical Society Series B: Statistical Methodology_, 58(1), 267-288.
