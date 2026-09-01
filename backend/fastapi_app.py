from fastapi import FastAPI
import pickle

app = FastAPI()

with open('Backend/best_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.get("/")
def welcome():
    return {"message": "SMS Spam Detection API Running"}

@app.post("/predict")
def predict(message: str):
    prediction = model.predict([message])[0]

    result = int(prediction)

    return {"prediction": result}