# Bati E-commerce Credit Model

## Overview
This project aims to develop a credit scoring model for an e-commerce platform, Bati, to evaluate the creditworthiness of customers. The model will help Bati to make informed decisions about lending and credit limits, reducing the risk of default and improving overall business performance.

## Project Structure
The project is organized into the following directories:

- **scripts**: Contains Python scripts for data preprocessing, feature engineering, model training, and evaluation.
- **notebooks**: Contains Jupyter notebooks for exploratory data analysis, data visualization, and model development.
- **app**: Contains the Django application for deploying the credit scoring model as a web service.
- **data**: Contains the dataset used for training and testing the model.
- **tests**: Contains unit tests for the project.
- **requirements**: Contains the dependencies required for the project.

## Dataset
The dataset used for this project is a sample dataset containing information about customers, transactions, and credit history. The dataset is anonymized and contains the following features:

- Customer ID
- Transaction ID
- Transaction date
- Transaction amount
- Product category
- Channel ID
- Pricing strategy
- Fraud result

## Methodology
The project follows the following methodology:

1. **Data Preprocessing**: The dataset is cleaned, transformed, and preprocessed to prepare it for modeling.
2. **Feature Engineering**: New features are created to improve the model's performance, such as aggregating transaction amounts and calculating RFMS scores.
3. **Model Training**: A credit scoring model is trained using a machine learning algorithm, such as logistic regression or random forest.
4. **Model Evaluation**: The model is evaluated using metrics such as accuracy, precision, recall, and F1-score.
5. **Model Deployment**: The trained model is deployed as a web service using Django.

## Scripts
The following scripts are used in the project:

- `eda_analysis.py`: Performs exploratory data analysis and data visualization.
- `feature_engineering.py`: Creates new features and preprocesses the data.
- `model_training.py`: Trains the credit scoring model.
- `model_evaluation.py`: Evaluates the model's performance.
- `app.py`: Deploys the model as a web service using Django.
- `logger.py`: Sets up logging for the project.
- `credit_scoring_model.py`: Contains the credit scoring model.

## Notebooks
The following notebooks are used in the project:

- `eda_analysis.ipynb`: Performs exploratory data analysis and data visualization.
- `model_development.ipynb`: Develops and trains the credit scoring model.

## App
The Django app is used to deploy the credit scoring model as a web service. The app contains the following files:

- `models.py`: Defines the database models for the app.
- `views.py`: Defines the views for the app, including the credit scoring model.
- `templates`: Contains the HTML templates for the app.
- `static`: Contains the static files for the app.
- `forms.py`: Defines the forms for the app.
- `urls.py`: Defines the URLs for the app.

## Tests
The project includes unit tests to ensure the correctness of the code. The tests are written using the unittest framework and are located in the tests directory.

## Requirements
The project requires the following dependencies:

- Python 3.8+
- Django 3.2+
- scikit-learn 1.0+
- pandas 1.3+
- numpy 1.20+
- matplotlib 3.4+
- seaborn 0.11+
- streamlit 0.86+

## Installation
To install the project, follow these steps:

1. Clone the repository using `git clone https://github.com/username/bati-ecommerce-credit-model.git`.
2. Install the dependencies using `pip install -r requirements.txt`.
3. Run the Django app using `python manage.py runserver`.

## Usage
To use the credit scoring model, follow these steps:

1. Open the Django app in a web browser.
2. Enter the customer ID and transaction information.
3. Click the "Predict" button to get the credit score.

## License
The project is licensed under the MIT License.

## Contributing
Contributions are welcome! To contribute to the project, follow these steps:

1. Fork the repository using `git fork https://github.com/username/bati-ecommerce-credit-model.git`.
2. Make changes to the code.
3. Commit the changes using `git commit -m "commit message"`.
4. Push the changes to the forked repository using `git push`.
5. Create a pull request to merge the changes into the main repository.

## Acknowledgments
The project uses the following libraries and frameworks:

- Django
- scikit-learn
- pandas
- numpy
