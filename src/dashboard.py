import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scripts.eda_analysis import (
    load_data, data_overview, summary_statistics, plot_numerical_distributions,
    plot_categorical_distributions, correlation_analysis, detect_outliers,
    bivariate_analysis, multivariate_analysis, time_series_analysis
)

# Streamlit App Title
st.title("Exploratory Data Analysis (EDA) Dashboard")

# Load the datasets
df = load_data('../data/data.csv')
variables = load_data('../data/Xente_Variable_Definitions.csv')

# Display the datasets
st.subheader("Dataset Preview")
st.write("Main Dataset (df):")
st.write(df.head())

st.write("Variable Definitions (variables):")
st.write(variables)

# Data Overview
st.subheader("Data Overview")
if st.button("Show Data Overview"):
    st.write("Dataset Shape:", df.shape)
    st.write("\nColumn Names:", df.columns.tolist())
    st.write("\nData Types:")
    st.write(df.dtypes)
    st.write("\nMissing Values:")
    st.write(df.isnull().sum())

# Summary Statistics
st.subheader("Summary Statistics")
if st.button("Show Summary Statistics"):
    st.write(summary_statistics(df))

# Numerical Distributions
st.subheader("Numerical Distributions")
if st.button("Plot Numerical Distributions"):
    st.pyplot(plot_numerical_distributions(df))

# Categorical Distributions
st.subheader("Categorical Distributions")
categorical_columns = st.multiselect("Select Categorical Columns", df.columns)
if st.button("Plot Categorical Distributions"):
    if categorical_columns:
        st.pyplot(plot_categorical_distributions(df, categorical_columns))
    else:
        st.warning("Please select at least one categorical column.")

# Correlation Analysis
st.subheader("Correlation Analysis")
if st.button("Show Correlation Matrix"):
    st.pyplot(correlation_analysis(df))

# Outlier Detection
st.subheader("Outlier Detection")
if st.button("Detect Outliers"):
    st.pyplot(detect_outliers(df))

# Bivariate Analysis
st.subheader("Bivariate Analysis")
if st.button("Perform Bivariate Analysis"):
    st.pyplot(bivariate_analysis(df))

# Multivariate Analysis
st.subheader("Multivariate Analysis")
if st.button("Perform Multivariate Analysis"):
    st.pyplot(multivariate_analysis(df))

# Time Series Analysis
st.subheader("Time Series Analysis")
if st.button("Perform Time Series Analysis"):
    st.pyplot(time_series_analysis(df))