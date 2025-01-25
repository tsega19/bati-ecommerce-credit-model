import unittest
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from your_module import (  # Replace 'your_module' with the actual module name
    load_data, data_overview, summary_statistics, plot_numerical_distributions,
    plot_categorical_distributions, correlation_analysis, detect_outliers,
    bivariate_analysis, time_series_analysis
)

class TestDataAnalysisFunctions(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Load sample data for testing
        cls.df = load_data('sample_data.csv')

    def test_load_data(self):
        self.assertIsInstance(self.df, pd.DataFrame)
        self.assertGreater(len(self.df), 0)

    def test_data_overview(self):
        # This test just checks if the function runs without errors
        data_overview(self.df)

    def test_summary_statistics(self):
        stats = summary_statistics(self.df)
        self.assertIsInstance(stats, pd.DataFrame)
        self.assertGreater(len(stats), 0)

    def test_plot_numerical_distributions(self):
        fig = plot_numerical_distributions(self.df)
        self.assertIsInstance(fig, plt.Figure)
        plt.close(fig)

    def test_plot_categorical_distributions(self):
        categorical_columns = ['ProductCategory', 'ChannelId']  # Example categorical columns
        fig = plot_categorical_distributions(self.df, categorical_columns)
        self.assertIsInstance(fig, plt.Figure)
        plt.close(fig)

    def test_correlation_analysis(self):
        fig = correlation_analysis(self.df)
        self.assertIsInstance(fig, plt.Figure)
        plt.close(fig)

    def test_detect_outliers(self):
        fig = detect_outliers(self.df)
        self.assertIsInstance(fig, plt.Figure)
        plt.close(fig)

    def test_bivariate_analysis(self):
        fig = bivariate_analysis(self.df)
        self.assertIsInstance(fig, plt.Figure)
        plt.close(fig)

    def test_time_series_analysis(self):
        fig = time_series_analysis(self.df)
        self.assertIsInstance(fig, plt.Figure)
        plt.close(fig)

if __name__ == '__main__':
    unittest.main()