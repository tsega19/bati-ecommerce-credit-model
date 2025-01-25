import sys
import os
import streamlit as st

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join('..', 'scripts')))

from scripts.eda_analysis import (
    load_data, data_overview, summary_statistics, plot_numerical_distributions,
    plot_categorical_distributions, correlation_analysis, detect_outliers,
    bivariate_analysis, time_series_analysis
)

# Streamlit App Title
st.title("Exploratory Data Analysis (EDA) Dashboard")

# Load the datasets
df = load_data('data/data.csv')
variables = load_data('data/Xente_Variable_Definitions.csv')

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
    fig = plot_numerical_distributions(df)
    st.pyplot(fig)  # Pass the figure to st.pyplot()

# Categorical Distributions
st.subheader("Categorical Distributions")
categorical_columns = st.multiselect("Select Categorical Columns", df.columns)
if st.button("Plot Categorical Distributions"):
    if categorical_columns:
        fig = plot_categorical_distributions(df, categorical_columns)
        st.pyplot(fig)  # Pass the figure to st.pyplot()
    else:
        st.warning("Please select at least one categorical column.")

# Correlation Analysis
st.subheader("Correlation Analysis")
if st.button("Show Correlation Matrix"):
    fig = correlation_analysis(df)
    st.pyplot(fig)  # Pass the figure to st.pyplot()

# Outlier Detection
st.subheader("Outlier Detection")
if st.button("Detect Outliers"):
    fig = detect_outliers(df)
    st.pyplot(fig)  # Pass the figure to st.pyplot()

# Bivariate Analysis
st.subheader("Bivariate Analysis")
if st.button("Perform Bivariate Analysis"):
    fig = bivariate_analysis(df)
    st.pyplot(fig)  # Pass the figure to st.pyplot()

# Time Series Analysis
st.subheader("Time Series Analysis")
if st.button("Perform Time Series Analysis"):
    fig = time_series_analysis(df)
    st.pyplot(fig)  # Pass the figure to st.pyplot()