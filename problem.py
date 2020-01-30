import os
import numpy as np
import pandas as pd
import rampwf as rw
from rampwf.workflows import FeatureExtractorRegressor
from rampwf.score_types.base import BaseScoreType
from sklearn.model_selection import GroupShuffleSplit

problem_title = 'Predicting number of accident'

# A type (class) which will be used to create wrapper objects for y_pred
Predictions = rw.prediction_types.make_regression(label_names=['n_collisions'])
workflow = rw.workflows.FeatureExtractorRegressor()

# An object implementing the workflow

# --------------------------------------------
# Scoring
# --------------------------------------------

# Normalized root mean square error

class NRMSE(BaseScoreType):
    is_lower_the_better = True
    minimum = 0.0
    maximum = np.inf

    def __init__(self, name='nrmse', precision=2):
        self.name = name
        self.precision = precision

    def __call__(self, y_true, y_pred):
        nrmse = 0
        for val_true, val_pred in zip(y_true, y_pred):
            if (val_true != 0):
                if val_pred < val_true:
                    nrmse += (((val_pred - val_true) / val_true) * 1.5) ** 2
                else:
                    nrmse += ((val_pred - val_true) / val_true) ** 2
            else:
                nrmse += val_pred ** 2
        return np.sqrt(nrmse / y_true.shape[0])[0]


class Precision(BaseScoreType):
    is_lower_the_better = False
    minimum = 0.0
    maximum = 1.0

    def __init__(self, name='prec', precision=2):
        self.name = name
        self.precision = precision

    def __call__(self, y_true, y_pred):
        y_pred_binary = np.vectorize(lambda x: 0 if (x == 0) else 1)(y_pred)
        y_true_binary = np.vectorize(lambda x: 0 if (x == 0) else 1)(y_true)
        score = precision_score(y_true_binary, y_pred_binary)
        return score


class Recall(BaseScoreType):
    is_lower_the_better = False
    minimum = 0.0
    maximum = 1.0

    def __init__(self, name='rec', precision=2):
        self.name = name
        self.precision = precision

    def __call__(self, y_true, y_pred):
        y_pred_binary = np.vectorize(lambda x: 0 if (x == 0) else 1)(y_pred)
        y_true_binary = np.vectorize(lambda x: 0 if (x == 0) else 1)(y_true)
        score = recall_score(y_true_binary, y_pred_binary)
        return score


score_types = [

    # Normalized root mean square error
    NRMSE(name='nrmse', precision=2),
    # Precision and recall
    Precision(name='prec', precision=2),
    Recall(name='rec', precision=2)

]


# --------------------------------------------
# Cross validation
# --------------------------------------------


def get_cv(X, y):
    cv = KFold(n_splits=5, random_state=45)
    # print("get_cv = ", cv.split(X, y))
    return cv.split(X, y)


#--------------------------------------------
# Data reader
#--------------------------------------------


def _read_data(path, f_name):
    data = pd.read_csv(os.path.join(path, 'data', f_name), low_memory=False,
                       compression='zip')
    y_array = data[_target_column_name].values
    X_df = data.drop(_target_column_name, axis=1)
    return X_df, y_array


def get_train_data(path='.'):
    f_name = 'company_revenue_TRAIN.csv.zip'
    return _read_data(path, f_name)


def get_test_data(path='.'):
    f_name = 'company_revenue_TEST.csv.zip'
    return _read_data(path, f_name)