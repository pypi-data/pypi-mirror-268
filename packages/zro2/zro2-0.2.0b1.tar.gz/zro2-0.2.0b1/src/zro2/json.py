
import json

def read_json(file : str):
    with open(file) as f:
        return json.load(f)
    
def write_json(file : str, data):
    with open(file, 'w') as f:
        json.dump(data, f, indent=4)

