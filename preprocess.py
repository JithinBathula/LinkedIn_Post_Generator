import json
def process_posts(raw_file_path, processed_file_path = "/data/processed.posts.json"):
    processed_posts_list = []
    with open(raw_file_path, encoding='utf-8') as file:
        posts = json.load(file)
        for post in posts:
            metadata = extract_info(post["description"])
            new_post = post | metadata
            processed_posts_list.append(new_post)
    
    print(processed_posts_list)

def extract_info(text):
    return {
        "line_count": 10
    }
if __name__ == "__main__":
    process_posts("data/raw_posts.json")