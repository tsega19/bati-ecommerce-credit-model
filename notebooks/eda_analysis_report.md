# Exploratory Data Analysis Report

## Overview
This report summarizes the findings from the exploratory data analysis (EDA) conducted on the dataset. The analysis includes data loading, overview, summary statistics, univariate analysis, correlation analysis, outlier detection, and fraud analysis.

## Data Loading
The dataset was successfully loaded, consisting of 95,662 rows and 16 columns with no missing values. The `TransactionDate` column was identified to require conversion to datetime format for time-based analysis.

## Data Overview
- **Duplicates**: There are no duplicate rows in the dataset.
- **Variable Definitions**: The variable definitions were printed for reference.

## Summary Statistics
- **CountryCode**: Constant across all records (value = 256).
- **Amount**: Ranges from -1,000,000 to 9,880,000 with a high standard deviation (approx. 123,307), indicating significant variability. The median (1,000) is much lower than the mean (6,717.846), suggesting a right-skewed distribution.
- **Value**: Similar to Amount, with a median (1,000) lower than the mean (9,900.584).
- **FraudResult**: 0.2018% of transactions labeled as fraudulent.

## Univariate Analysis
### Distribution of Numerical Features
- Numerical distributions were plotted to visualize the spread of numerical features.

### Distribution of Categorical Features
- Categorical distributions were plotted for specified columns: `CurrencyCode`, `ProviderId`, `ProductId`, `ProductCategory`, and `ChannelId`.

## Correlation Analysis
- Correlation analysis was performed to identify relationships between numerical features.

## Outlier Detection
- Outliers were detected using box plots for numerical columns.

## Fraud Analysis
- A pie chart was generated to visualize the distribution of fraud vs. non-fraud transactions.

## Bivariate and Multivariate Analysis
- Bivariate and multivariate analyses were conducted to explore relationships between variables.

## Time Series Analysis
- Time series analysis was performed to understand trends over time.

## Conclusion
The exploratory data analysis provided valuable insights into the dataset, highlighting key statistics, distributions, and potential areas for further investigation.
