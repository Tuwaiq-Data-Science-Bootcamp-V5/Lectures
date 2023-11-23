from pydantic import BaseModel

class Passenger(BaseModel):
    pclass: int
    sex: str
    age: int
    sibsp: int
    parch: int
    fare: float
    S: int
    C: int
    Q: int