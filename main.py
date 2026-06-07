from Linear_regression_01.components.data_ingestion import DataIngestion
from Linear_regression_01.pipeline.stage_01_DI import DataIngestionTrainingPipeline
from Linear_regression_01.logging import logger

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>> Stage {STAGE_NAME} Started <<<<<<<<<<")
    data_injestion = DataIngestionTrainingPipeline()
    data_injestion.main()
    logger.info(f">>>>>>>>> Stage {STAGE_NAME} Completed <<<<<<<<<<")

except Exception as e:
    logger.exception(e)
    raise e