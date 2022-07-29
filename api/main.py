from fastapi import FastAPI
from .app.models import PredictionRequest, PredictionResponse
from .app.views import get_classification


app = FastAPI(docs_url='/')

@app.post('/classification')
def make_classification(request: PredictionRequest):
    return PredictionResponse(pass_type=get_classification(request))

