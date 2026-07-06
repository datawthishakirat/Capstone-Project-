# 🌍 Predicting Carbon Dioxide (CO₂) Emissions Using Socioeconomic and Environmental Indicators

## 📌 Project Overview

This project was completed as the final capstone project for the **AnalystLab Africa Data Science Internship**.

The objective is to predict national **carbon dioxide (CO₂) emissions per capita** using socioeconomic and environmental indicators from the **World Bank World Development Indicators (WDI)** dataset. The project follows the complete data science workflow, including data preparation, exploratory data analysis, machine learning, model evaluation, and deployment using Streamlit.

---

## 🎯 Problem Statement

Governments worldwide aim to reduce greenhouse gas emissions while sustaining economic growth. However, economic development, energy consumption and urbanization often contribute to increasing CO₂ emissions.

This project investigates whether selected development indicators can accurately predict national CO₂ emissions and provide insights to support evidence-based environmental policy and sustainable development.

---

## 📊 Dataset

**Source:** World Bank World Development Indicators (WDI)

https://datatopics.worldbank.org/world-development-indicators/

The analysis uses the **2023** data.

### Selected Features

- Access to electricity (% of population)
- Energy use (kg of oil equivalent per capita)
- Forest area (% of land area)
- GDP per capita (current US$)
- Urban population (% of total population)

### Target Variable

- Carbon dioxide (CO₂) emissions excluding LULUCF per capita (t CO₂e/capita)

---

## 🛠 Technologies Used Python, Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn,
Joblib, Streamlit

---

## 📈 Project Workflow

1. Data Collection
2. Data Cleaning and Preprocessing
3. Exploratory Data Analysis (EDA)
4. Feature Selection
5. Model Development
6. Model Evaluation
7. Streamlit Deployment

---

## 🤖 Machine Learning Models

Two regression models were developed:

- Linear Regression
- Random Forest Regressor

### Model Performance

| Model | MAE | RMSE | R² |
|------|------:|------:|------:|
| Linear Regression | 1.69 | 2.17 | 0.52 |
| Random Forest | 2.71 | 7.43 | -4.64 |

The **Linear Regression** model achieved the best performance and was selected as the final model.

---

## 📌 Key Findings

- Energy use showed the strongest positive relationship with CO₂ emissions.
- GDP per capita had a moderate positive relationship with emissions.
- Urban population also contributed positively to emissions.
- Forest area showed a relatively weak relationship.
- Linear Regression outperformed Random Forest on this dataset.

---

## 💡 Recommendations

- Increase investment in renewable energy.
- Promote sustainable urban planning.
- Improve energy efficiency.
- Strengthen environmental data collection and reporting.

---

## 🚀 Streamlit Application

The project includes an interactive Streamlit application that allows users to:

- Select a country
- View its development indicators
- Modify indicator values
- Predict CO₂ emissions using the trained Linear Regression model

Run the application locally with:

```bash
streamlit run app.py
```

---

## 📂 Repository Structure

```
├── Capstone_Project.ipynb
├── app.py
├── linear_regression_model.pkl
├── predictors.pkl
├── medians.pkl
├── country_data.csv
├── README.md
└── Project_Report.pdf
```

## 👩‍💻 Author

**Shakirat Dabiri**

Data Science Enthusiast | Environmental Sustainability Researcher


---

## Acknowledgement

This project was completed as part of the **AnalystLab Africa Data Science Internship Program** using the **World Bank World Development Indicators (WDI)** dataset.
