# LinkedIn Post Generator (LLM-Focused)

This repository demonstrates a **Large Language Model (LLM)**–driven workflow for generating LinkedIn-style posts. By leveraging prompt engineering techniques, JSON output parsing, and a few-shot approach, it showcases how LLMs can efficiently process and generate text in real-world applications.

## Introduction

This project began as a way to automate the creation of LinkedIn posts for various authors. However, the emphasis quickly turned to exploring **LLM capabilities**—both for **NLP-based data preprocessing** (tag unification, metadata extraction) and for **content generation** (LinkedIn posts with specific style and tone).

By reading this, you should gain insight into:
- How to **prompt-engineer** LLMs for data cleaning and extraction.  
- How to build a **few-shot learning** mechanism in generating new posts that match an existing author’s style.  
- How to integrate everything into a **Streamlit** app for easy user interaction.

---

## Key LLM Components

1. **ChatGroq**: We leverage [ChatGroq](https://groq.com/) as our LLM backend.  
2. **Prompt Engineering**:  
   - **Unifying Tags**: A carefully crafted prompt merges similar tags into a consolidated taxonomy.  
   - **Extracting Post Metadata**: Another prompt that detects language, counts lines, and generates up to two tags per post.  
   - **Generating LinkedIn Posts**: A final prompt that uses few-shot examples to replicate an author’s style while focusing on a specific topic and length.  

3. **JSON Output Parser**: Ensures LLM responses are structured and parseable (especially for tasks like data cleaning).

---

## Features

- **LLM-Based Data Processing**:  
  - Converts raw CSV exports into JSON.  
  - Uses an LLM to unify tags (merging synonyms).  
  - Extracts post metadata (line count, language) via a prompt.  

- **Few-Shot Learning for Post Generation**:  
  - Dynamically filters existing posts as examples based on the user’s desired author, topic, and length.  
  - The LLM uses these examples to reproduce a consistent style.  

- **Interactive Streamlit App**:  
  - Allows users to pick an **Author**, filter the **Topic** automatically, and choose a **Length** (Short, Medium, Long).  
  - One-click generation of LinkedIn posts via an LLM prompt.  

---

## Setup & Installation

1. **Clone the Repository**:

2. **Create & Activate a Virtual Environment** (Optional but recommended):

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**:
   - Create a `.env` file (or modify if provided):
     ```
     API_KEY=your-llm-api-key-here
     ```
   - This key is used by `llm_helper.py` to authenticate with the LLM (ChatGroq).

---

## Data Preprocessing with LLMs

### 1. Convert CSV → JSON
1. Update file paths in **`convert_csv_to_json.py`**:
   ```python
   filepaths = ["data/satyanadella.csv", "data/BillGates.csv", "data/JeffWeiner.csv"]
   json_file_path = "data/raw_posts.json"
   convert_csv_to_json(filepaths, json_file_path)
   ```
2. Run:
   ```bash
   python preprocessing_scripts/convert_csv_to_json.py
   ```
   This creates **`data/raw_posts.json`**.

### 2. LLM-Driven Tag Unification & Metadata Extraction
1. Check **`preprocess_posts.py`** for two major LLM prompts:  
   - **`get_unified_tags()`**: merges similar tags into a single canonical tag (prompt instructions + JSON output parsing).  
   - **`extract_info()`**: uses an LLM to count lines, detect language, and assign up to two tags per post.
2. Run:
   ```bash
   python preprocess_posts.py
   ```
   This script:
   - Reads `data/raw_posts.json`.
   - Calls ChatGroq with carefully designed prompts.
   - Outputs the final **`data/processed_posts.json`** with standardized tags and metadata.

---

## Generating Posts with LLM (Few-Shot Learning)

**`post_generator.py`** contains the logic for generating LinkedIn posts:
```python
def generate_post(similar_post, author, topic, length):
    ...
    # 1) Build a prompt that includes:
    #    - Topic, length, and author instructions
    #    - (Optional) A few-shot list of examples from `similar_post`
    # 2) Invoke the LLM (ChatGroq) with the final prompt
    # 3) Return the text response
```

**Few-Shot**: The script selects existing posts (filtered by the author, topic, and length criteria) as examples. The LLM uses these as references to mimic the style while generating new content.

---

## Streamlit App Usage

**`main.py`** is the entry point for the Streamlit application:
1. **Author Selection**: A dropdown to choose from the authors in `processed_posts.json`.  
2. **Topic Selection**: Dynamically filtered to display only tags used by that author.  
3. **Length Selection**: Short, Medium, or Long.  
4. **Generate Button**: Calls `generate_post(...)` with few-shot examples if available.  

To run the app:
```bash
streamlit run main.py
```
Then open [localhost:8501](http://localhost:8501/) in your browser.  

---

## Acknowledgements
- **Posts Export for LinkedIn** extension for helping scrape data directly from LinkedIn to CSV.  
- **YouTube Tutorial**: [https://youtu.be/qZ_J-Xg0QM4](https://youtu.be/qZ_J-Xg0QM4) for teaching the basics and inspiring this project idea.

---
