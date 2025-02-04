import unittest
from scripts.credit_scoring_model import create_preprocessing_pipeline, extract_date_features


class TestCreditScoringModel(unittest.TestCase):

    def test_create_preprocessing_pipeline(self):
        pipeline = create_preprocessing_pipeline()
        self.assertIsNotNone(pipeline)

    def test_extract_date_features(self):
        data = pd.DataFrame({'TransactionStartTime': ['2018-01-01 00:00:00']})
        features = extract_date_features(data)
        self.assertIn('TransactionDay', features.columns)
        self.assertIn('TransactionMonth', features.columns)
        self.assertIn('TransactionYear', features.columns)


if __name__ == '__main__':
    unittest.main()
