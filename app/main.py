from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def display():
    return "Hello world is changed to hello universe"