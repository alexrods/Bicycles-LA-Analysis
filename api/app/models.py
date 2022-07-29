from pandas import Timestamp
from pydantic import BaseModel


class PredictionRequest(BaseModel):
    trip_id: int
    duration: int
    start_time: Timestamp
    end_time: Timestamp
    start_lat: float
    start_lon: float
    end_lat: float
    end_lon: float
    bike_id: str
    trip_route_category: str
    start_station: int
    end_station: int


class PredictionResponse(BaseModel):
    pass_type: int
    

