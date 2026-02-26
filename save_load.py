import json

FILE_PATH = 'data/characters.json'

def load_characters():
    try:
        with open(FILE_PATH, 'r') as file:
            data = json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return {}
    
    return data

def save_characters(data):
    with open(FILE_PATH, 'w') as file:
        json.dump(data, file, indent= 2)