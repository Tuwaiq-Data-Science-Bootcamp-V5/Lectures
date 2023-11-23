from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def welcome():
    return "Welcome To Tuwaiq"

@app.get("/add")
def add(x1: int, x2: int):
    return x1+x2
