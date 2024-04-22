import requests
import json
import pandas as pd
import numpy as np

if __name__ == "__main__":

    url = "http://127.0.0.1:8000/scheduler/post_person/"
    file = "../data/roster.csv"

    df = pd.read_csv(file)

    for i in range(len(df)):
        row = df.iloc[i]
        req = {
            "name": row["name"],
            "short_name": row["short_name"],
            "email": row["email"],
            "role": None
        }
        print(req)
        print(requests.post(url, json=req).text)