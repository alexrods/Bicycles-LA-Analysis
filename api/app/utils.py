import pickle
from pandas import DataFrame
from pydantic import BaseModel
from sklearn.pipeline import Pipeline


def get_model() -> Pipeline:
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