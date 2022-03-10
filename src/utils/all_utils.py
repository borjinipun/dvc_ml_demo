 
import yaml
import os


def read_yaml(path_to_yaml: str) -> dict:
    with open(path_to_yaml) as yaml_files:
        content = yaml.safe_load(yaml_files)

    return content
