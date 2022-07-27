import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin


class FeaturesEngineering(BaseEstimator, TransformerMixin):
    '''
    This class makes multiple transformations to the dataset
    
    '''
    def __init__(self):
        pass

    def fit(self, X: pd.DataFrame, y=None):
        return self            

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
 
        X.fillna(method='ffill')
        X['month'] = X['start_time'].apply(lambda x: x.month)
        X['day'] = X['start_time'].apply(lambda x: x.weekday())
        X['hour'] = X['start_time'].apply(lambda x: x.hour)


        X.drop(['trip_id', 'start_time', 'end_time', 'bike_id', 
                'start_station', 'end_station'], axis=1, inplace=True)

        return X


def prepare_dataset(data: pd.DataFrame) -> pd.DataFrame:
    
    data.dropna(subset='passholder_type', inplace=True)    
    data = data[data['duration'] < 1000]
    data = data[data['start_lat'] < 40.0]
    data = data[data['start_lon'] < -100.0]
    data = data[data['end_lat'] < 40.0]
    data = data[data['end_lon'] < -100.0]

    return data 