import streamlit as st
from pipeline.pipeline import AnimeRecommendationPipeline

from dotenv import load_dotenv


st.set_page_config(page_title=  "Anime Recommendation System", page_icon=":sparkles:", layout="wide")

load_dotenv()


@st.cache_resource
def init_pipeline():
    """Initialize the recommendation pipeline."""
    return AnimeRecommendationPipeline()

pipeline = init_pipeline()

st.title("Anime Recommendation System")
st.markdown("Welcome to the Anime Recommendation System! :sparkles:")
st.markdown("This application recommends anime based on your preferences. :sparkles:")

query = st.text_input("Enter your anime preferences eg. : liht hearted anime with comedy")
if query:
    with st.spinner("Generating recommendations..."):
        response = pipeline.recommend(query)
        st.markdown("### Recommendations:")
        st.write(response)
        
