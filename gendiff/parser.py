import json
import yaml
import os.path


def parse(file):
    file_format = os. path.splitext(file)[1]
    if file_format == '.json':
        return json.load(open(file))
    elif file_format == '.yml' or '.yaml':
        return yaml.safe_load(open(file))
    else:
        raise AttributeError
