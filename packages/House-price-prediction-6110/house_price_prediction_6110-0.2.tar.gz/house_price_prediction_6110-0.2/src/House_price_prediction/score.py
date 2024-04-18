"""
This script scores trained machine learning models for regression tasks using linear regression, decision tree regression, and random forest regression.

Functions:
    score_linear_regression(housing_prepared, housing_labels): Scores a linear regression model.
    score_decision_tree_regressor(housing_prepared, housing_labels): Scores a decision tree regression model.
    score_random_forest(housing_prepared, housing_labels): Scores a random forest regression model.

Constants:
    None

Dependencies:
    - argparse
    - os
    - pickle
    - numpy
    - ingest_data (imported as load_testing_data)
    - sklearn.metrics (imported as mean_absolute_error, mean_squared_error)

Usage:
    The script expects a filename as an argument indicating the dataset to use for testing. It loads the testing data and the trained models, then scores each model using mean squared error (MSE) and mean absolute error (MAE).

Example:
    python score.py test.csv
"""

import argparse
import os
import pickle

import numpy as np

# from ingest_data import load_testing_data
from sklearn.metrics import mean_absolute_error, mean_squared_error


def score_linear_regression(housing_prepared, housing_labels):
    """
    Scores a linear regression model.

    Args:
        housing_prepared (pandas.DataFrame): Prepared features of the housing data.
        housing_labels (pandas.Series): Labels of the housing data.
    """
    try:
        lin_reg = pickle.load(open("../../artifacts/lin_reg_model.pkl", "rb"))
        housing_predictions = lin_reg.predict(housing_prepared)
        lin_mse = mean_squared_error(housing_labels, housing_predictions)
        lin_rmse = np.sqrt(lin_mse)
        lin_mae = mean_absolute_error(housing_labels, housing_predictions)
        print("lin_rmse: ", lin_rmse, "\nlin_mae: ", lin_mae)
        return lin_rmse, lin_mae
    except Exception as e:
        print(e)
        return None, None


def score_decision_tree_regressor(housing_prepared, housing_labels):
    """
    Scores a decision tree regression model.

    Args:
        housing_prepared (pandas.DataFrame): Prepared features of the housing data.
        housing_labels (pandas.Series): Labels of the housing data.
    """
    try:
        tree_reg = pickle.load(open("../../artifacts/tree_reg_model.pkl", "rb"))
        housing_predictions = tree_reg.predict(housing_prepared)
        tree_mse = mean_squared_error(housing_labels, housing_predictions)
        tree_rmse = np.sqrt(tree_mse)
        print("tree_rmse: ", tree_rmse)
        return tree_mse
    except Exception as e:
        print(e)
        return None


def score_random_forest(housing_prepared, housing_labels):
    """
    Scores a random forest regression model.

    Args:
        housing_prepared (pandas.DataFrame): Prepared features of the housing data.
        housing_labels (pandas.Series): Labels of the housing data.
    """
    try:
        final_model = pickle.load(open("../../artifacts/final_model.pkl", "rb"))
        final_predictions = final_model.predict(housing_prepared)
        final_mse = mean_squared_error(housing_labels, final_predictions)
        final_rmse = np.sqrt(final_mse)
        print("final_rmse: ", final_rmse)
        return final_rmse
    except Exception as e:
        print(e)
        return None


# if __name__ == "__main__":
#     parser = argparse.ArgumentParser()
#     parser.add_argument(
#         "fileName", help="name of the file you want to use for training"
#     )
#     args = parser.parse_args()
#     X, y = load_testing_data(
#         args.fileName, os.path.join("../../datasets/housing/processed")
#     )
#     score_linear_regression(X, y)
#     score_decision_tree_regressor(X, y)
#     score_random_forest(X, y)
