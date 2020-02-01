import os
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import FunctionTransformer
from sklearn.pipeline import Pipeline


class FeatureExtractor(object):
    def __init__(self):
        pass

    def fit(self, X_df, y_array):
        meteo_jour = pd.read_csv('./data/meteo_jour.csv')
        meteo_jour["jour"] = pd.to_datetime(meteo_jour["jour"], dayfirst=True).dt.date

        def process_date(X):
            date = pd.to_datetime(X['Date'])
            return np.c_[date.dt.year, date.dt.month, date.dt.day, date.dt.hour]
        date_transformer = FunctionTransformer(process_date, validate=False)



        temp_cols = ['temp_high', 'temp_avg', 'temp_low',
               'dew_point_high', 'dew_point_avg', 'dew_point_low', 'humidity_high',
               'humidity_avg', 'humidity_low', 'speed_high', 'speed_avg', 'speed_low',
               'pressure_high', 'pressure_low', 'precipitation_acc']

        def merge(X):
            X["jour"] = pd.to_datetime(X['Date']).dt.date
            df = pd.merge(X, meteo_jour, left_on='jour',
                          right_on='jour', how='left')

            return df[temp_cols]

        merge_transformer = FunctionTransformer(merge, validate=False)



        drop_cols = ["t_1h"]
        date_cols = ["Date"]
        merge_col = ["Date"]

        preprocessor = ColumnTransformer(
            transformers=[
                ('merge', make_pipeline(merge_transformer,
                                        SimpleImputer(strategy='median')), merge_col),
                ('date', make_pipeline(date_transformer,
                                       SimpleImputer(strategy='median')), date_cols),
                ('drop cols', 'drop', drop_cols),

            ])



        self.preprocessor = preprocessor
        self.preprocessor.fit(X_df, y_array)
        return self

    def transform(self, X_df):
        return self.preprocessor.transform(X_df)

