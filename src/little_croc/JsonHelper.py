import json


def write_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
