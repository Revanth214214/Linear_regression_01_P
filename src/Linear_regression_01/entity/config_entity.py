from dataclasses import dataclass
from pathlib import Path
from typing import List, Dict

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    ALL_REQUIRED_FILES: List[str]
    all_schema: Dict[str, str]

@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    STATUS_FILE: Path