from src.vector_store import VectorStoreBuilder
from src.recommender import AnimeRecommender

from config.config import GROQ_API_KEY, MODEL_NAME

from utils.custom_exception import CustomException
from utils.logger import get_logger

logger = get_logger(__name__)

class AnimeRecommendationPipeline:
    def __init__(self, persist_dir="chroma_db"):
        try:
            logger.info("Initializing AnimeRecommendationPipeline...")
            vector_builder = VectorStoreBuilder(
                csv_path="",
                persist_dir=persist_dir
            )

            retriever = vector_builder.load_vector_store().as_retriever()
            self.recommender = AnimeRecommender(
                retriever=retriever,
                api_key=GROQ_API_KEY,
                model_name=MODEL_NAME
            )

            logger.info("AnimeRecommendationPipeline initialized successfully.")

        except Exception as e:
            logger.error(f"Error initializing AnimeRecommendationPipeline: {e}")
            raise CustomException("Failed to initialize AnimeRecommendationPipeline") from e
        
    def recommend(self, query:str):
        try:
            logger.info(f"Generating recommendations for query: {query}")
            recommendations = self.recommender.get_recommendation(query)
            logger.info(f"Recommendations generated successfully for query: {query}")
            return recommendations
        except Exception as e:
            logger.error(f"Error generating recommendations for query '{query}': {e}")
            raise CustomException("Failed to generate recommendations") from e
