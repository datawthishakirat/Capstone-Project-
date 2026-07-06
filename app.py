import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# PAGE SETTINGS
# -----------------------------
st.set_page_config(
    page_title="CO₂ Emissions Prediction Dashboard",
    page_icon="🌍",
    layout="wide"
)

# -----------------------------
# LOAD FILES
# -----------------------------
model = joblib.load("linear_regression_model.pkl")

df = pd.read_csv("country_data.csv")

target = "Carbon dioxide (CO2) emissions excluding LULUCF per capita (t CO2e/capita)"

predictors = [
    "Access to electricity (% of population)",
    "Energy use (kg of oil equivalent per capita)",
    "Forest area (% of land area)",
    "GDP per capita (current US$)",
    "Urban population (% of total population)"
]

# -----------------------------
# SIDEBAR
# -----------------------------

st.sidebar.title("Project Information")

st.sidebar.write("""
### World Bank WDI Capstone Project

**Topic**

Predicting Carbon Dioxide (CO₂) Emissions Using Socioeconomic and Environmental Indicators

**Model**

Linear Regression

**Dataset**

World Bank World Development Indicators (2023)

**Developer**

Shakirat Dabiri
""")

st.sidebar.markdown("---")

st.sidebar.write("### Model Performance")

st.sidebar.metric("MAE", "1.69")
st.sidebar.metric("RMSE", "2.17")
st.sidebar.metric("R²", "0.52")

# -----------------------------
# TITLE
# -----------------------------

st.title("🌍 CO₂ Emissions Prediction Dashboard")

st.write("""
Select a country, modify its development indicators if desired,
and predict CO₂ emissions using a trained Linear Regression model.
""")

# -----------------------------
# COUNTRY
# -----------------------------

country = st.selectbox(
    "Select Country",
    sorted(df["Country Name"])
)

country_data = df[df["Country Name"] == country].iloc[0]

# -----------------------------
# CURRENT COUNTRY VALUES
# -----------------------------

st.subheader("Current Country Indicators")

col1, col2 = st.columns(2)

with col1:

    electricity = st.number_input(
        "Access to Electricity (%)",
        value=float(country_data[predictors[0]])
    )

    energy = st.number_input(
        "Energy Use (kg oil equivalent per capita)",
        value=float(country_data[predictors[1]])
    )

    forest = st.number_input(
        "Forest Area (%)",
        value=float(country_data[predictors[2]])
    )

with col2:

    gdp = st.number_input(
        "GDP per Capita (US$)",
        value=float(country_data[predictors[3]])
    )

    urban = st.number_input(
        "Urban Population (%)",
        value=float(country_data[predictors[4]])
    )

# -----------------------------
# PREDICT
# -----------------------------

if st.button("Predict CO₂ Emissions"):

    X = pd.DataFrame([[
        electricity,
        energy,
        forest,
        gdp,
        urban
    ]], columns=predictors)

    prediction = model.predict(X)[0]

    actual = country_data[target]

    st.success(
        f"Predicted CO₂ Emissions: **{prediction:.2f} t CO₂e per capita**"
    )

    st.info(
        f"Actual 2023 CO₂ Emissions: **{actual:.2f} t CO₂e per capita**"
    )

    difference = prediction - actual

    if difference > 0:

        st.warning(
            f"The prediction is **{difference:.2f} t CO₂e** higher than the reported value."
        )

    else:

        st.success(
            f"The prediction is **{abs(difference):.2f} t CO₂e** lower than the reported value."
        )

# -----------------------------
# KEY FINDINGS
# -----------------------------

st.markdown("---")

st.header("Key Findings")

st.markdown("""
- Energy use had the strongest positive relationship with CO₂ emissions.
- GDP per capita showed a moderate positive relationship.
- Urban population was positively associated with emissions.
- Forest area showed a relatively weak relationship.
- Linear Regression outperformed Random Forest.
""")

# -----------------------------
# RECOMMENDATIONS
# -----------------------------

st.header("Recommendations")

st.markdown("""
- Increase investment in renewable energy.
- Promote sustainable urban planning.
- Improve environmental monitoring.
- Increase data availability for future prediction models.
""")

# -----------------------------
# FOOTER
# -----------------------------

st.markdown("---")

st.caption("Capstone Project • World Bank WDI Dataset")