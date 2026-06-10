from Linear_regression_01.config.configuration import configurationManager
from Linear_regression_01.components.data_validation import DataValidation
from Linear_regression_01.logging import logger

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = configurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        
        files_ok = data_validation.validate_all_files_exists()
        if files_ok:
            data_validation.validate_all_columns()
            logger.info("Data Validation completed successfully.")
        else:
            logger.error("Data Validation failed.")
