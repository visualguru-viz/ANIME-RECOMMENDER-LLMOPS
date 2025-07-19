from src.data_loader import AnimeDataLoader
from src.vector_store import VectorStoreBuilder

from dotenv import load_dotenv

from utils.logger import get_logger
from utils.custom_exception import CustomException

load_dotenv()

logger = get_logger(__name__)

def main():
    try:
        logger.info("Starting Anime Recommendation Pipeline build process...")

        # Load data
        loader = AnimeDataLoader("data/anime_with_synopsis.csv", "data/anime_updated.csv")
        processed_csv = loader.load_and_process()

        logger.info("Data loaded and processed successfully.")
    
        # Build vector store
        vector_builder = VectorStoreBuilder(processed_csv)
        vector_builder.build_and_save_vector_store()

        logger.info("Vector store built and saved successfully.")

        logger.info("Anime Recommendation Pipeline build process completed successfully.")

    except Exception as e:
        logger.error(f"Error during pipeline build: {e}")
        raise CustomException("Failed to build Anime Recommendation Pipeline") from e
    

if __name__ == "__main__":
    main()
    