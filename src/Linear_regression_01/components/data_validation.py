import os
import pandas as pd
import urllib.request as request
import tarfile
from Linear_regression_01.logging import logger
from Linear_regression_01.utils.common import get_size
from Linear_regression_01.entity.config_entity import DataIngestionConfig
from Linear_regression_01.entity.config_entity import DataValidationConfig
from pathlib import Path

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    # simple python code that validates all files

    def validate_all_files_exists(self) -> bool:
        try:
            validation_status = None

            all_files = os.listdir(os.path.join("artifacts", "data_ingestion"))

            for file in all_files:
                if file not in self.config.ALL_REQUIRED_FILES:
                    validation_status = False
                    with open(self.config.STATUS_FILE, "w") as f:
                        f.write(f"validation status: {validation_status}")
                
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, "w") as f:
                        f.write(f"validation status: {validation_status}")

            return validation_status
            
        except Exception as e:
            raise e

    #function to validate against the schema     
    def validate_all_columns(self) -> bool:
        try:
            validation_status = True  # Assume true until proven otherwise

            path_to_csv = os.path.join("artifacts","data_ingestion","housing.csv")

            df = pd.read_csv(path_to_csv)
            all_cols = list(df.columns)
            
            # 2. Grab the expected schema columns
            schema_cols = self.config.all_schema.keys()
            
            # 3. Check every column in the dataset against the schema
            for col in all_cols:
                if col not in schema_cols:
                    validation_status = False
                    break
            
            # 4. Append the result to your status tracking file
            with open(self.config.STATUS_FILE, "a") as f:
                f.write(f"Column schema validation status: {validation_status}\n")
                
            return validation_status
            
        except Exception as e:
            raise e