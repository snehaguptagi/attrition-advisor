# Employee Attrition Analysis

An end-to-end exploratory data analysis and machine-learning study of **employee attrition** — why people voluntarily leave an organization, and whether it can be predicted from HR data.

> 📓 The full analysis lives in [`Attrition_Analysis.ipynb`](Attrition_Analysis.ipynb) (63 cells, with charts and model results inline). Open it on [Colab](https://colab.research.google.com/github/snehaguptagi/sneha.com/blob/main/Attrition_Analysis.ipynb) or locally with Jupyter.

## What's inside

**Exploratory analysis**
- Attrition reasons and their relative frequency
- Attrition by seniority, gender (≈1,197 male / 216 female employees), and tenure (departures peak in the **first year**)
- Engagement scores: active vs. inactive employees
- Promotion vs. attrition (≈21% attrition among promotion-eligible employees)
- Performance-band analysis and feature binning

**Modelling**
- Preprocessing: `StandardScaler`, feature selection (`SelectPercentile`), train/test split
- Class imbalance handled with **SMOTE** (`imblearn`)
- Models compared: Logistic Regression, Decision Tree, KNN, SVC, Gaussian Naive Bayes, AdaBoost, **XGBoost**
- Evaluation via confusion matrices and F1 scores

## Tech stack

`pandas` · `numpy` · `scikit-learn` · `xgboost` · `imbalanced-learn` · `matplotlib` · `seaborn` · `plotly`

## Run it

```bash
pip install -r requirements.txt
jupyter notebook Attrition_Analysis.ipynb
```

## Notes

- The notebook ships with its outputs (charts, tables) rendered inline, so you can read the findings without re-running it.
- Built as a portfolio data-science project.
