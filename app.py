from fastapi import FastAPI
import pandas as pd


app = FastAPI()
# model = pickle.load(open("model_v2.pkl", "rb"))
games_list = pd.read_csv("similar_item.csv")


@app.get("/")
async def root():
    return {"message": "hello hello"}


@app.get("/predict/{game_id}")
async def predict(game_id: int):
    final = games_list[games_list["src_game_id"] == game_id]
    return final.to_dict(orient="records")
