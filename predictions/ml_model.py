import pickle
from typing import Dict
from urllib import request
import joblib
from sklearn.ensemble import RandomForestClassifier


def joblib_load_model() -> RandomForestClassifier:
    filename = "predictions/model_rf_joblib.sav"
    model = joblib.load(filename)
    return model
    
    
def predict_if_will_win(request_data: Dict) -> bool:
    model = joblib_load_model()
    data = [
        int(request_data.get("InternalTeamId")),
        int(request_data.get("Map")),
        int(request_data.get("RoundId")),
        float(request_data.get("RoundStartingEquipmentValue")),
        float(request_data.get("TeamStartingEquipmentValue")),
        float(request_data.get("MatchKills")),
        float(request_data.get("MatchAssists")),
    ]
    print(data)
    prediction = model.predict([data])
    print(prediction)
    return prediction[0]
