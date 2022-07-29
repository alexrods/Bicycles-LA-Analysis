from .models import PredictionRequest
from .tools import get_model, transform_to_df


model = get_model()

def get_classification(request: PredictionRequest) -> int:
    to_predict = transform_to_df(request)
    prediction = model.predict(to_predict)

    return max(0, prediction)
