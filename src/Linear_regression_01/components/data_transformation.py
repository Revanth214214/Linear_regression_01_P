import os
import pandas as pd
import urllib.request as request
import tarfile
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from Linear_regression_01.logging import logger
from Linear_regression_01.utils.common import get_size
from Linear_regression_01.entity.config_entity import DataIngestionConfig
from Linear_regression_01.entity.config_entity import DataValidationConfig
from Linear_regression_01.entity.config_entity import DataTransformationConfig
from pathlib import Path


class DataTransformation:
    def __init__(self, data_transformation_config):
        self.config = data_transformation_config
    
    def check_validation_status(self) -> bool:
        with open(self.config.STATUS_FILE, "r") as f:
            status = f.read().split(" ")[-1].strip()
            
        if status == "True":
            return True
        else:
            return False
    
    def initiate_data_transformation(self):
        #check the schema validation from prev functon
        if self.check_validation_status():
            #read raw data (stg_1)
            df = pd.read_csv(self.config.data_path)
            
            #split data
            train, test = train_test_split(df, test_size=0.2, random_state=42)
            
            #save data files to path
            train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
            test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)
            
            print("Data split into training and testing sets successfully.")
            print(f"Train shape: {train.shape}, Test shape: {test.shape}")
            
        else:
            raise Exception("Data Validation Stage failed! Cannot proceed with Data Transformation.")