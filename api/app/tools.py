import os
import pickle
from io import BytesIO
from joblib import load
from pandas import DataFrame
from pydantic import BaseModel
from sklearn.pipeline import Pipeline


def get_model() -> Pipeline:
    # model_path = os.environ.get('MODELS_PATH','model/model.pkl')
    # with open(model_path, 'rb') as model_file:
    #     model = load(BytesIO(model_file.read()))
    model = Pipeline
    with open('model/model.pkl', 'rb') as model_file:
        while True:
            try:
                model = pickle.load(model_file)
            except EOFError:
                break
    return model

    


def transform_to_df(class_model: BaseModel) -> DataFrame:
    request_dict = {key: [value] for key, value in class_model.dict().items()}
    df = DataFrame(request_dict)

    return df