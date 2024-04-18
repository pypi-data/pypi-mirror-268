"""
This script provides functions for fetching, loading, preprocessing, and splitting housing data.

Functions:
    fetch_housing_data(housing_url, housing_path): Downloads housing data from a URL and extracts it to a specified path.
    load_housing_data(housing_path): Loads housing data from a CSV file.
    load_testing_data(fileName, housing_path): Loads processed testing data from a CSV file.
    load_training_data(fileName, housing_path): Loads processed training data from a CSV file.
    income_cat_proportions(data): Computes the proportions of income categories in the data.
    get_labels_and_data(housing_df): Processes housing data, imputes missing values, and encodes categorical variables.
    preProcessing(housing_path): Preprocesses the housing data by stratified splitting and saves as CSV files.

Constants:
    DOWNLOAD_ROOT: Root URL for downloading the housing dataset.
    HOUSING_PATH: Directory path for storing housing data.
    HOUSING_URL: URL of the housing dataset.
"""

# import argparse
import os
import tarfile

import numpy as np
import pandas as pd
from six.moves import urllib
from sklearn.impute import SimpleImputer
from sklearn.model_selection import StratifiedShuffleSplit

DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml/master/"
HOUSING_PATH = os.path.join("../datasets/housing")
HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"


def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):
    """
    Downloads housing data from a URL and extracts it to a specified path.

    Args:
        housing_url (str): URL of the housing dataset.
        housing_path (str): Directory path for storing housing data.
    """
    try:
        os.makedirs(housing_path, exist_ok=True)
        tgz_path = os.path.join(housing_path, "housing.tgz")
        urllib.request.urlretrieve(housing_url, tgz_path)
        housing_tgz = tarfile.open(tgz_path)
        housing_tgz.extractall(path=housing_path + "/original")
        housing_tgz.close()
    except Exception as e:
        print(e)


def load_housing_data(housing_path=HOUSING_PATH):
    """
    Loads housing data from a CSV file.

    Args:
        housing_path (str): Directory path for storing housing data.

    Returns:
        pandas.DataFrame: Loaded housing data.
    """
    try:
        csv_path = os.path.join(housing_path, "housing.csv")
        return pd.read_csv(csv_path)
    except Exception as e:
        print(e)


def load_testing_data(fileName, housing_path=HOUSING_PATH + "/processed"):
    """
    Loads processed testing data from a CSV file.

    Args:
        fileName (str): Name of the CSV file containing testing data.
        housing_path (str): Directory path for storing processed housing data.

    Returns:
        tuple: A tuple containing processed testing data and labels.
    """
    try:
        csv_path = os.path.join(housing_path, fileName)
        df = pd.read_csv(csv_path)
        return get_labels_and_data(df)
    except Exception as e:
        print(e)


def load_training_data(fileName, housing_path=HOUSING_PATH + "/processed"):
    """
    Loads processed training data from a CSV file.

    Args:
        fileName (str): Name of the CSV file containing training data.
        housing_path (str): Directory path for storing processed housing data.

    Returns:
        tuple: A tuple containing processed training data and labels.
    """
    try:
        csv_path = os.path.join(housing_path, fileName)
        print(csv_path)
        df = pd.read_csv(csv_path)
        return get_labels_and_data(df)
    except Exception as e:
        print(e)


def income_cat_proportions(data):
    """
    Computes the proportions of income categories in the data.

    Args:
        data (pandas.DataFrame): Input data.

    Returns:
        pandas.Series: Proportions of income categories.
    """
    try:
        return data["income_cat"].value_counts() / len(data)
    except Exception as e:
        print(e)


def get_labels_and_data(housing_df):
    """
    Processes housing data, imputes missing values, and encodes categorical variables.

    Args:
        housing_df (pandas.DataFrame): Input housing data.

    Returns:
        tuple: A tuple containing processed data and labels.
    """
    try:
        # drop labels for training set
        housing = housing_df.drop("median_house_value", axis=1)
        housing_labels = housing_df["median_house_value"].copy()

        housing_num = housing.drop("ocean_proximity", axis=1)

        imputer = SimpleImputer(strategy="median")

        imputer.fit(housing_num)
        X = imputer.transform(housing_num)

        housing_tr = pd.DataFrame(X, columns=housing_num.columns, index=housing.index)
        housing_tr["rooms_per_household"] = (
            housing_tr["total_rooms"] / housing_tr["households"]
        )
        housing_tr["bedrooms_per_room"] = (
            housing_tr["total_bedrooms"] / housing_tr["total_rooms"]
        )
        housing_tr["population_per_household"] = (
            housing_tr["population"] / housing_tr["households"]
        )
        housing_cat = housing[["ocean_proximity"]]
        housing_prepared = housing_tr.join(pd.get_dummies(housing_cat, drop_first=True))

        return (housing_prepared, housing_labels)
    except Exception as e:
        print(e)


def preProcessing(housing_path=HOUSING_PATH):
    """
    Preprocesses the housing data by stratified splitting and saves as CSV files.

    Args:
        housing_path (str): Directory path for storing housing data.
    """
    try:
        housing = load_housing_data(housing_path + "/original")
        housing["income_cat"] = pd.cut(
            housing["median_income"],
            bins=[0.0, 1.5, 3.0, 4.5, 6.0, np.inf],
            labels=[1, 2, 3, 4, 5],
        )

        split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
        for train_index, test_index in split.split(housing, housing["income_cat"]):
            strat_train_set = housing.loc[train_index]
            strat_test_set = housing.loc[test_index]

        # train_set, test_set = train_test_split(housing, test_size=0.2, random_state=42)

        for set_ in (strat_train_set, strat_test_set):
            set_.drop("income_cat", axis=1, inplace=True)

        os.makedirs(HOUSING_PATH + "/processed", exist_ok=True)

        strat_train_set.to_csv(
            HOUSING_PATH + "/processed/train.csv",
            index=False,
        )
        strat_test_set.to_csv(HOUSING_PATH + "/processed/test.csv", index=False)
    except Exception as e:
        print(e)


# if __name__ == "__main__":
#     fetch_housing_data()
#     preProcessing()

#     print("Done")
