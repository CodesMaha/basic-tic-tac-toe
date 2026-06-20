""" write and read user data from data.json """

import json

PATH: str = "core/data.json"

def write_data(data: dict) -> None:
    with open(PATH, "w") as f:
        json.dump(data, f)

def reset_data() -> dict:
    data: dict = {"x_score": 0, "o_score": 0}
    write_data(data)
    return data

def read_data() -> dict:
    try: # EAFP
        with open(PATH, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = reset_data()
    return data

def increment_score(winner: str) -> None:
    """ increase score of x or o by one """
    data = read_data()
    data[f"{winner}_score"] += 1
    write_data(data)