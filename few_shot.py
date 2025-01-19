import json
import pandas as pd
class Few_Shots_Post:
    def  __init__(self, filepath = "data/processed_posts.json"):
        self.df = None
        self.unique_tags = None
        self.load_posts(filepath)

    def load_posts(self, filepath):
        with open(filepath, encoding="utf-8") as file:
            posts = json.load(file)
            df = pd.json_normalize(posts)
            df["length"] = df["line_count"].apply(self.length_calc)
        
            print(df)

    
    def length_calc(self, line_count):
        if (line_count <3):
            return "Short"
        elif (line_count < 5):
            return "Medium"
        else:
            return "Long"
        

if __name__ ==  "__main__":
    f = Few_Shots_Post()