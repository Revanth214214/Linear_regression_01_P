import os
import urllib.request as request
import tarfile
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
    
    def extract_zip_file(self):
        """
        Extracts the tgz file into the unzip directory
        """
        unzip_path = "artifacts/data_ingestion"
        os.makedirs(unzip_path, exist_ok=True)

        logger.info(f"Extracting {self.config.local_data_file} to {unzip_path}...")
        with tarfile.open(self.config.local_data_file, "r:gz") as tar_ref:
            tar_ref.extractall(path=unzip_path)
        logger.info("Extraction complete!")