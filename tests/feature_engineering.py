import unittest
from scripts.feature_engineering import *

class TestFeatureEngineering(unittest.TestCase):
    def setUp(self):
        self.df = pd.read_csv('data/data.csv')

    def test_encode_categorical_variables(self):
        df = encode_categorical_variables(self.df)
        self.assertEqual(df.shape, (95662, 24))

    def test_create_numerical_features(self):
        df = create_numerical_features(self.df)
        self.assertEqual(df.shape, (95662, 30))

    def test_handle_missing_values(self):
        df = handle_missing_values(self.df)
        self.assertEqual(df.shape, (95662, 24))

if __name__ == '__main__':
    unittest.main()
