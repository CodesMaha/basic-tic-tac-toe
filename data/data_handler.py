""" write and read user data from data.json """

import json

class DataHandler:
    def __init__(self, file_path: str, resetted_data: dict):
        # init with empty vals
        self.path = file_path
        self.resetted = resetted_data
    
    def write(self, data: dict) -> None:
        with open(self.path, "w") as f:
            json.dump(data, f)

    def reset(self) -> dict:
        """ reset json file then return resetted data """
        self.write(self.resetted)
        return self.resetted
    
    def read(self) -> dict:
        try: # EAFP
            with open(self.path, "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            data = self.reset()
        return data

class ScoreData(DataHandler):
    def __init__(self):
        super().__init__("data/score.json", {"x_score": 0, "o_score": 0})
    
    def increment_score(self, winner: str) -> None:
        """ increment score of either x or o by one """
        data = self.read()
        data[f"{winner}_score"] += 1
        self.write(data)

# TODO: MENACE feature still in progress! store training with this class
class MatchboxesData(DataHandler):
    def __init__(self):
        super().__init__("data/score.json", {})