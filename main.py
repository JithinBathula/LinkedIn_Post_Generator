import streamlit as st
from few_shot import Few_Shots_Post
from post_generator import generate_post
def main():
    st.title("LinkedIn Post")
    col1, col2, col3 = st.columns(3)
    f = Few_Shots_Post()
    with col1:
        author = st.selectbox("Author", options=f.get_authors())
    with col2:
        if author:
            topic = st.selectbox("Topic", options=f.get_author_tags(author))
        else:
            topic = st.selectbox("Topic", options=[])
    with col3:
        length = st.selectbox("Length", options=["Short", "Medium", "Long"])

    if st.button("Generate"):
        st.write(f"Generating the perfect LinkedIn Post based on {topic}, {length} and {author}")
        similar_posts = f.get_filtered_posts(length, author,topic)
        
        st.write(generate_post(similar_posts, author, topic, length))
    
if __name__ == "__main__":
    main()