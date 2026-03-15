# Adv Crop Prediction APP

![Language](https://img.shields.io/badge/Language-Jupyter%20Notebook-DA5B0B?style=flat-square) ![Stars](https://img.shields.io/github/stars/Devanik21/ADV-crop-prediction-app?style=flat-square&color=yellow) ![Forks](https://img.shields.io/github/forks/Devanik21/ADV-crop-prediction-app?style=flat-square&color=blue) ![Author](https://img.shields.io/badge/Author-Devanik21-black?style=flat-square&logo=github)

> Precision agriculture meets predictive intelligence — forecast crop yield and health from soil and climate features.

---

## Overview

An end-to-end machine learning web application that ingests agronomic parameters — soil pH, temperature, rainfall, humidity, and fertilizer data — and outputs crop-type recommendations or yield estimates via a trained classification/regression pipeline. Built on Streamlit for zero-friction deployment and instant interactivity.

**Topics:** `precision-agriculture` · `agricultural-ai` · `classification` · `data-science` · `deep-learning` · `machine-learning` · `neural-networks` · `random-forest-regressor` · `streamlit` · `crop-yield-forecasting`

---

## Features

- Multi-feature agronomic input interface with real-time validation
- Trained ML model (RandomForest / XGBoost) served via Streamlit
- Prediction confidence scores and feature importance visualisation
- Responsive layout compatible with mobile and desktop browsers
- CSV batch-prediction support for bulk field analysis

---

## Tech Stack

Primary stack: Jupyter Notebook, Python. Key libraries: Streamlit, scikit-learn, pandas, NumPy, Matplotlib/Plotly. Model serialisation via `joblib` or `pickle`.

**Key dependencies detected:** `streamlit` · `pandas` · `numpy` · `scikit-learn` · `joblib` · `matplotlib` · `seaborn` · `xgboost` · `lightgbm` · `tensorflow`

---

## Getting Started

```bash
pip install streamlit scikit-learn pandas numpy plotly
streamlit run app.py
```

---

## Project Structure

```
ADV-crop-prediction-app/
├── README.md
├── requirements.txt

├── notebooks/

└── ...
```

---

## Author

**Devanik Debnath**  
B.Tech, Electronics & Communication Engineering  
National Institute of Technology Agartala

[![GitHub](https://img.shields.io/badge/GitHub-Devanik21-black?style=flat-square&logo=github)](https://github.com/Devanik21)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-devanik-blue?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/devanik/)

---

*Built with curiosity, precision, and a love for building things that matter.*
