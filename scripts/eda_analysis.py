import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path):
    """Load the dataset from a CSV file."""
    return pd.read_csv(file_path, index_col=False)

def data_overview(df):
    """Provide an overview of the dataset."""
    print("Dataset Shape:", df.shape)
    print("\nColumn Names:", df.columns.tolist())
    print("\nData Types:")
    print(df.dtypes)
    print("\nMissing Values:")
    print(df.isnull().sum())

def summary_statistics(df):
    """Calculate and return summary statistics for numerical columns."""
    return df.describe()

def plot_numerical_distributions(df):
    """Plot distributions of numerical features and return the figure."""
    numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
    n_cols = 2
    n_rows = (len(numerical_cols) + 1) // 2  # ensure enough rows for all plots
    
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, 5*n_rows))
    axes = axes.flatten()

    for i, col in enumerate(numerical_cols):
        sns.histplot(df[col], kde=True, ax=axes[i], color='blue')
        axes[i].set_title(f'Distribution of {col}')
        axes[i].set_xlabel(col)
        axes[i].set_ylabel('Count')
    
    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    plt.tight_layout()
    return fig  # Return the figure instead of showing it

def plot_categorical_distributions(df, columns):
    """Plot distributions of specified categorical features and return the figure."""
    categorical_cols = [col for col in columns if df[col].dtype == 'object']  # Filter only categorical columns
    n_cols = 2
    n_rows = (len(categorical_cols) + 1) // 2  # ensure enough rows for all plots
    
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, 5*n_rows))
    axes = axes.flatten()

    for i, col in enumerate(categorical_cols):
        df[col].value_counts().plot(kind='bar', ax=axes[i])
        axes[i].set_title(f'Distribution of {col}')
        axes[i].set_xlabel(col)
        axes[i].set_ylabel('Count')
        axes[i].tick_params(axis='x', rotation=45)

    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    plt.tight_layout()
    return fig  # Return the figure instead of showing it

def correlation_analysis(df):
    """Perform correlation analysis on numerical features and return the figure."""
    numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
    corr_matrix = df[numerical_cols].corr()

    fig, ax = plt.subplots(figsize=(12, 10))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5, ax=ax)
    plt.title('Correlation Matrix of Numerical Features')
    return fig  # Return the figure instead of showing it

def detect_outliers(df):
    """Detect outliers using box plots for numerical features and return the figure."""
    numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
    n_cols = 2
    n_rows = (len(numerical_cols) + 1) // 2
    
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, 5*n_rows))
    axes = axes.flatten()

    for i, col in enumerate(numerical_cols):
        sns.boxplot(x=df[col], ax=axes[i])
        axes[i].set_title(f'Box Plot of {col}')
        axes[i].set_xlabel(col)
    
    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    plt.tight_layout()
    return fig  # Return the figure instead of showing it

def bivariate_analysis(df):
    """Perform bivariate analysis and return the figure."""
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    
    # 1. Amount vs Product Category
    sns.boxplot(x='ProductCategory', y='Amount', data=df, ax=axes[0, 0])
    axes[0, 0].set_title('Transaction Amount by Product Category')
    axes[0, 0].tick_params(axis='x', rotation=45)
    
    # 2. Fraud Rate by Product Category
    fraud_rate = df.groupby('ProductCategory')['FraudResult'].mean()
    fraud_rate.sort_values(ascending=False).plot(kind='bar', ax=axes[0, 1])
    axes[0, 1].set_title('Fraud Rate by Product Category')
    axes[0, 1].set_ylabel('Fraud Rate')
    axes[0, 1].tick_params(axis='x', rotation=45)
    
    # 3. Fraud vs Amount
    sns.boxplot(x='FraudResult', y='Amount', data=df, ax=axes[1, 0])
    axes[1, 0].set_title('Transaction Amount for Fraudulent vs Non-Fraudulent Transactions')
    
    # 4. ChannelId vs Amount
    channel_avg_amount = df.groupby('ChannelId')['Amount'].mean().sort_values(ascending=False)
    channel_avg_amount.plot(kind='bar', ax=axes[1, 1])
    axes[1, 1].set_title('Average Transaction Amount by Channel')
    axes[1, 1].set_ylabel('Average Amount')
    axes[1, 1].tick_params(axis='x', rotation=45)
    
    plt.tight_layout()
    return fig  # Return the figure instead of showing it

def time_series_analysis(df):
    """Perform time series analysis and return the figure."""
    df['TransactionStartTime'] = pd.to_datetime(df['TransactionStartTime'])
    df['Date'] = df['TransactionStartTime'].dt.date
    daily_transactions = df.groupby('Date')['Amount'].sum().reset_index()
    
    fig, axes = plt.subplots(2, 1, figsize=(12, 12))
    
    # 1. Daily Transaction Volume
    axes[0].plot(daily_transactions['Date'], daily_transactions['Amount'])
    axes[0].set_title('Daily Transaction Volume')
    axes[0].set_xlabel('Date')
    axes[0].set_ylabel('Total Amount')
    axes[0].tick_params(axis='x', rotation=45)
    
    # 2. Hourly Transactions
    df['Hour'] = df['TransactionStartTime'].dt.hour
    hourly_transactions = df.groupby('Hour').size()
    hourly_transactions.plot(kind='bar', ax=axes[1])
    axes[1].set_title('Number of Transactions by Hour of Day')
    axes[1].set_xlabel('Hour')
    axes[1].set_ylabel('Number of Transactions')
    
    plt.tight_layout()
    return fig  # Return the figure instead of showing it