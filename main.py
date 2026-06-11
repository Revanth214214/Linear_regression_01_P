from Linear_regression_01.components.data_ingestion import DataIngestion
from Linear_regression_01.components.data_validation import DataValidation
from Linear_regression_01.pipeline.stage_01_DI import DataIngestionTrainingPipeline
from Linear_regression_01.pipeline.stage_02_DV import DataValidationTrainingPipeline
from Linear_regression_01.pipeline.stage_03_DT import DataTransformationTrainingPipeline
from Linear_regression_01.logging import logger

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>> Stage {STAGE_NAME} Started <<<<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>>> Stage {STAGE_NAME} Completed <<<<<<<<<<")

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f">>>>>> Stage {STAGE_NAME} Started <<<<<<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>>>>> Stage {STAGE_NAME} Completed <<<<<<<<<<")

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f">>>>>> Stage {STAGE_NAME} Started <<<<<<<<<<")
    data_validation = DataTransformationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>>>>> Stage {STAGE_NAME} Completed <<<<<<<<<<")

except Exception as e:
    logger.exception(e)
    raise e