import os
from box.exceptions import BoxValueError
import yaml
from src.Text_Summarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Read yaml file and returns a ConfigBox instance
    
    Args:
        path_to_yaml (str): Path to yaml file

    Raises: 
        ValueError: If the yaml file does not exist or is not valid
        e: empty file

    Returns:
        ConfigBox: A ConfigBox instance with the loaded data
    """

    try:
        with open(path_to_yaml, 'r') as file:
            content = yaml.safe_load(file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("Yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Create a list of directories

    Args:
        path_to_directories (list): List of directories to be created
        verbose (bool, optional): Whether to print the creation messages. Defaults to True.
    """
    for directory in path_to_directories:
        if not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)
            if verbose:
                logger.info(f"Created directory: {directory}")
                