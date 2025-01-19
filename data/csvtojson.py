import csv
import json

def convert_csv_to_json(csv_file_path_list, json_file_path):

    json_data = []
    for csv_file_path in csv_file_path_list:
        try:
            with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
                csv_reader = csv.DictReader(csv_file)

                for row in csv_reader:
                    json_entry = {
                        "description": row["text"],
                        "engagement": {
                            "likes": int(row["likes"]),
                            "comments": int(row["comments"]),
                            "shares": int(row["shares"])
                        },
                        "name": row["fullName"]


                    }
                    json_data.append(json_entry)

        except Exception as e:
            print(f"An error occurred: {e}")
        
    with open(json_file_path, mode='w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file, indent=4)
    print(f"JSON data has been successfully written to {json_file_path}")


filepaths = ["data/satyanadella.csv" , "data/BillGates.csv", "data/JeffWeiner.csv"  ]
csv_file_path = "data/satyanadella.csv" 
json_file_path = "data/raw_posts.json"  
convert_csv_to_json(filepaths, json_file_path)
