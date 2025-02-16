import json
from llm_helper import llm
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException

def process_posts(raw_file_path, processed_file_path = "data/processed_posts.json"):
    processed_posts_list = []
    with open(raw_file_path, encoding='utf-8') as file:
        posts = json.load(file)
        for post in posts:
            metadata = extract_info(post["description"])
            new_post = post | metadata
            processed_posts_list.append(new_post)
    
    unified_tags = get_unified_tags(processed_posts_list)

    for post in processed_posts_list:
        tags = post["tags"]
        for i in range(len(tags)):
            tags[i] = unified_tags[tags[i]]
        
        post["tags"] = list(set(tags))

    
    with open(processed_file_path, encoding='utf-8', mode='w') as outfile:
        json.dump(processed_posts_list, outfile, indent=4)

def get_unified_tags(posts):
    unique_tags = set()
    for post in posts:
        unique_tags.update(post["tags"])


    unique_tags_string = ",".join(unique_tags)

    prompt_template = '''You are tasked with unifying a list of tags according to specific requirements. Your goal is to create a shorter, more consolidated list of tags by merging similar concepts. Here are the detailed instructions:

    1. You will be provided with a list of tags in the following format:
    {tags}

    2. Review the list of tags and think through the unification process. Consider the following requirements:
    a. Merge tags that represent similar concepts. For example:
        - "Jobseekers" and "Job Hunting" can be merged into "Job Search"
        - "Motivation", "Inspiration", and "Drive" can be mapped to "Motivation"
        - "Personal Growth", "Personal Development", and "Self Improvement" can be mapped to "Self Improvement"
        - "Scam Alert" and "Job Scam" can be mapped to "Scams"
    b. Ensure each unified tag follows title case convention (e.g., "Job Search", "Motivation")

    3. Create a JSON object that maps each original tag to its unified tag. The format should be:
    {{"Original Tag 1": "Unified Tag", "Original Tag 2": "Unified Tag", ...}}

    4. Your output should be the JSON object only, with no additional text or explanation.

    5. If an original tag doesn't need to be merged or changed, map it to itself in title case.

    Think through the unification process carefully, considering similar concepts and how they can be grouped together effectively. Once you have determined the unified tags, create the JSON object with the mappings.

    Provide your answer in the following format:
    {{JSON object with mappings}}'''

    print(unique_tags_string)

    pt = PromptTemplate.from_template(prompt_template)
    chain = pt | llm
    response = chain.invoke(input = {"tags": unique_tags})

    try:
        jsonparser = JsonOutputParser()
        res = jsonparser.parse(response.content)
    except:
        raise OutputParserException("Context too big")
    
    return res


def extract_info(text):

    prompt_template = '''You are tasked with analyzing a LinkedIn post and extracting specific information from it. Your goal is to provide a JSON output containing the line count, language, and tags of the post. Follow these instructions carefully:

        1. Here is the LinkedIn post you need to analyze: {post}

        2. Count the number of lines in the post. Consider any text separated by line breaks as a new line. Empty lines should be counted.

        3. Identify the primary language of the post.

        4. Extract up to two relevant tags from the post content. Tags should be single words or short phrases that represent the main topics or themes of the post. Do not include hashtag symbols (#) in the tags.

        5. Format your output as a JSON object with the following structure:
        
        {{
            "line_count": number of lines,
            "language": language code",
            "tags": ["tag1", "tag2"]
        }}

        6. Ensure that your JSON output is valid and contains exactly three keys: line_count, language, and tags. The tags array should contain a maximum of two elements.

        7. Provide only the JSON output without any additional text, explanations, or preamble.

        Begin your analysis now and output the resulting JSON.'''
    
    pt = PromptTemplate.from_template(prompt_template)
    chain = pt | llm
    response = chain.invoke(input ={'post': text})
    try:
        jsonparser = JsonOutputParser()
        res = jsonparser.parse(response.content)
    except:
        raise OutputParserException("Context too big")
    
    return res

if __name__ == "__main__":
    process_posts("data/raw_posts.json")
