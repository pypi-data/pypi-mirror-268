"""
This script trains machine learning models for regression tasks using linear regression, decision tree regression, and random forest regression.

Functions:
    train_linear_regression(housing_prepared, housing_labels): Trains a linear regression model.
    train_decision_tree_regressor(housing_prepared, housing_labels): Trains a decision tree regression model.
    train_random_forest(housing_prepared, housing_labels): Trains a random forest regression model.

Constants:
    None

Dependencies:
    - argparse
    - os
    - pickle
    - numpy
    - ingest_data (imported as load_training_data)
    - scipy.stats (imported as randint)
    - sklearn.ensemble (imported as RandomForestRegressor)
    - sklearn.linear_model (imported as LinearRegression)
    - sklearn.model_selection (imported as GridSearchCV, RandomizedSearchCV)
    - sklearn.tree (imported as DecisionTreeRegressor)

Usage:
    The script expects a filename as an argument indicating the dataset to use for training. It loads the training data, trains three regression models, and saves the trained models as pickle files in the 'artifacts' directory.

Example:
    python train.py train.csv
"""

import argparse
import os
import pickle

import numpy as np

# from ingest_data import load_training_data
from scipy.stats import randint
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn.tree import DecisionTreeRegressor


def train_linear_regression(housing_prepared, housing_labels):
    """
    Trains a linear regression model.

    Args:
        housing_prepared (pandas.DataFrame): Prepared features of the housing data.
        housing_labels (pandas.Series): Labels of the housing data.
    """
    try:
        lin_reg = LinearRegression()
        lin_reg.fit(housing_prepared, housing_labels)
        print("Done Linear Regression")
        return pickle.dump(lin_reg, open("../../artifacts/lin_reg_model.pkl", "wb"))
    except Exception as e:
        print(e)


def train_decision_tree_regressor(housing_prepared, housing_labels):
    """
    Trains a decision tree regression model.

    Args:
        housing_prepared (pandas.DataFrame): Prepared features of the housing data.
        housing_labels (pandas.Series): Labels of the housing data.
    """
    try:
        tree_reg = DecisionTreeRegressor(random_state=42)
        tree_reg.fit(housing_prepared, housing_labels)
        print("Done Decision Tree")
        return pickle.dump(tree_reg, open("../../artifacts/tree_reg_model.pkl", "wb"))
    except Exception as e:
        print(e)


def train_random_forest(housing_prepared, housing_labels):
    """
    Trains a random forest regression model.

    Args:
        housing_prepared (pandas.DataFrame): Prepared features of the housing data.
        housing_labels (pandas.Series): Labels of the housing data.
    """
    try:
        param_distribs = {
            "n_estimators": randint(low=1, high=200),
            "max_features": randint(low=1, high=8),
        }

        forest_reg = RandomForestRegressor(random_state=42)
        rnd_search = RandomizedSearchCV(
            forest_reg,
            param_distributions=param_distribs,
            n_iter=10,
            cv=5,
            scoring="neg_mean_squared_error",
            random_state=42,
        )
        rnd_search.fit(housing_prepared, housing_labels)
        cvres = rnd_search.cv_results_
        for mean_score, params in zip(cvres["mean_test_score"], cvres["params"]):
            print(np.sqrt(-mean_score), params)

        param_grid = [
            # try 12 (3×4) combinations of hyperparameters
            {"n_estimators": [3, 10, 30], "max_features": [2, 4, 6, 8]},
            # then try 6 (2×3) combinations with bootstrap set as False
            {"bootstrap": [False], "n_estimators": [3, 10], "max_features": [2, 3, 4]},
        ]

        forest_reg = RandomForestRegressor(random_state=42)
        # train across 5 folds, that's a total of (12+6)*5=90 rounds of training
        grid_search = GridSearchCV(
            forest_reg,
            param_grid,
            cv=5,
            scoring="neg_mean_squared_error",
            return_train_score=True,
        )
        grid_search.fit(housing_prepared, housing_labels)

        grid_search.best_params_
        cvres = grid_search.cv_results_
        for mean_score, params in zip(cvres["mean_test_score"], cvres["params"]):
            print(np.sqrt(-mean_score), params)

        feature_importances = grid_search.best_estimator_.feature_importances_
        sorted(zip(feature_importances, housing_prepared.columns), reverse=True)

        final_model = grid_search.best_estimator_
        return pickle.dump(final_model, open("../../artifacts/final_model.pkl", "wb"))
    except Exception as e:
        print(e)


# if __name__ == "__main__":
#     parser = argparse.ArgumentParser()
#     parser.add_argument(
#         "fileName", help="name of the file you want to use for training"
#     )
#     args = parser.parse_args()
#     print(args.fileName)
#     X, y = load_training_data(
#         args.fileName, os.path.join("../../datasets/housing/processed")
#     )

#     train_linear_regression(X, y)
#     train_decision_tree_regressor(X, y)
#     train_random_forest(X, y)
