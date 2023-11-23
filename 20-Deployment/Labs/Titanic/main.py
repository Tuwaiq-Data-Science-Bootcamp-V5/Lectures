from fastapi import FastAPI
from Passenger import Passenger
import pickle

app = FastAPI()

model = pickle.load(open("ml_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))


@app.post("/predict")
def predict(passenger: Passenger):
    passenger.sex = passenger.sex.lower()
    if(passenger.sex == "male"):
        passenger.sex = 0
    else:
        passenger.sex = 1


    X = [[
        passenger.pclass,
        passenger.sex,
        passenger.age,
        passenger.sibsp,
        passenger.parch,
        passenger.fare,
        passenger.C,
        passenger.Q,
        passenger.S
    ]]


    X = scaler.transform(X)
    Y = model.predict(X)[0]

    return {
        "survived": bool(Y)
    }
