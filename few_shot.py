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
            self.df = pd.json_normalize(posts)
            self.df["length"] = self.df["line_count"].apply(self.length_calc)
            all_tags = self.df["tags"].sum()
            self.unique_tags = list(set(all_tags))
    
    def length_calc(self, line_count):
        if (line_count <3):
            return "Short"
        elif (line_count < 5):
            return "Medium"
        else:
            return "Long"
        
    def get_tags(self):
        return self.unique_tags
    
    def get_authors(self):
        return list(set(list(self.df["name"])))
    
    def get_author_tags(self, author):
        filtered_df = self.df[self.df["name"] == author]

        author_tags = filtered_df["tags"].sum()
        return list(set(author_tags))

    def get_filtered_posts(self, length, name, tag):

        filtered = self.df[
            (self.df["length"] == length) &
            (self.df["name"] == name) &
            (self.df["tags"].apply(lambda tags:tag in tags))
        ]

        return filtered.to_dict(orient="records")
    

if __name__ ==  "__main__":
    f = Few_Shots_Post()