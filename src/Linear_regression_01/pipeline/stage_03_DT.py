from Linear_regression_01.config.configuration import configurationManager
from Linear_regression_01.logging import logger
from Linear_regression_01.components.data_transformation import DataTransformation

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = configurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(data_transformation_config)
    
        #run chek 1
        validation_true = data_transformation.check_validation_status()

        if validation_true:
            data_transformation.initiate_data_transformation()
            print("Data Transformation stage completed successfully")
        else:
            print("Data Transformation stage failed: recheck")