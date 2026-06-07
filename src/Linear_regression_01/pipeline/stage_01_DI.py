from Linear_regression_01.config.configuration import configurationManager
from Linear_regression_01.components.data_ingestion import DataIngestion
from Linear_regression_01.logging import logger

class DataIngestionTrainingPipeline:
    def __init__ (self):
        pass

    def main(self):
        config = configurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config = data_ingestion_config)
        data_ingestion.download_files()