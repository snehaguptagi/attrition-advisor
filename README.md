# Employee Attrition Analysis

An end-to-end study of **employee attrition** — why people voluntarily leave an organization — plus a **Claude-powered Attrition Risk Advisor** built on top of the analysis.

> 📓 The full analysis lives in [`Attrition_Analysis.ipynb`](Attrition_Analysis.ipynb) (63 cells, with charts and model results inline). Open it on [Colab](https://colab.research.google.com/github/snehaguptagi/employee-attrition-analysis/blob/main/Attrition_Analysis.ipynb) or locally with Jupyter.

## 🧠 Attrition Risk Advisor (AI tool)

[`app.py`](app.py) is a small Streamlit app on top of the analysis: HR enters an employee's attributes (the same factors the study used — tenure, engagement, performance, potential, promotion status), and **Claude** returns a risk read, the driving factors, and concrete retention actions — grounded in the study's real findings (first-year tenure is highest-risk, low engagement compounds it, ~21% of promotion-eligible employees still left).

```bash
pip install -r requirements.txt
streamlit run app.py          # add your Anthropic key in the sidebar
```

It's an AI advisor that reasons from the study's patterns — an HR triage aid, not an automated decision-maker, and not a model served on private data.

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
