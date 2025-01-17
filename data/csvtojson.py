import csv
import json

def convert_csv_to_json(csv_file_path, json_file_path):
    try:
        with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            json_data = []
            for row in csv_reader:
                json_entry = {
                    "description": row["text"],
                    "engagement": {
                        "likes": int(row["likes"]),
                        "comments": int(row["comments"]),
                        "shares": int(row["shares"])
                    }
                }
                json_data.append(json_entry)

        with open(json_file_path, mode='w', encoding='utf-8') as json_file:
            json.dump(json_data, json_file, indent=4)

        print(f"JSON data has been successfully written to {json_file_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Usage example
csv_file_path = "data/satyanadella.csv" 
json_file_path = "data/raw_posts.json"  
convert_csv_to_json(csv_file_path, json_file_path)
