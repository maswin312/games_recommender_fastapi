import pickle

# import implicit
import pandas as pd

model = pickle.load(open("model_v2.pkl", "rb"))
id, score = model.similar_items(228, 11)
results = pd.DataFrame({"game_id": id, "score": score})
print(results)
