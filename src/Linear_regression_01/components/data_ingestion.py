import os
import urllib.request as request
import zipfile
from Linear_regression_01.logging import logger
from Linear_regression_01.utils.common import get_size
from Linear_regression_01.entity.config_entity import DataIngestionConfig
from pathlib import Path

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config


    def download_files(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} Downloaded with following info \n{headers}")
        else:
            logger.info(f"file already exist of size: {get_size(Path(self.config.local_data_file))}")