from llm_helper import llm
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from langchain_core.prompts import PromptTemplate

def get_length_str(length):
    if length == "Short":
        return "1 to 5 lines"
    if length == "Medium":
        return "6 to 10 lines"
    if length == "Long":
        return "11 to 15 lines"
    
def generate_post(similar_post, author, topic, length):
    new_length = get_length_str(length)
    prompt = f'''
    You are tasked with generating a LinkedIn post based on specific input parameters. Your goal is to create an engaging and professional post that adheres to the given requirements.

    1) Topic: {topic}
    2) Length: {new_length}
    3) author: {author}

    1. The post should be written in English.
    2. Ensure the content is relevant to the given topic.
    3. Adhere to the specified length requirement.
    4. Write the post as if it were authored by the person mentioned in the author field.
    5. Do not include hashtags unless they are organically part of the writing style in the examples if provided.
    6. Avoid using emojis unless they are consistently used in the provided examples, if provided.
    '''

    if len(similar_post) > 0:
        prompt += "7) Use the writing style demonstrated in the examples provided below."

    for i, post in enumerate(similar_post):
        post_text = post['description']
        prompt += f'\n\n Example {i+1}: \n\n {post_text}'

    prompt += "Generate only the LinkedIn post. Do not generate any explanations or comments. Do not generate any LinkedIn Link either."    
    response = llm.invoke(prompt)
    return response.content

    
    
