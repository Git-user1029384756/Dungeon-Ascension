import json

FILE_PATH = 'data/characters.json'

def load_characters():
    try:
        with open(FILE_PATH, 'r') as file:
            data = json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return {}
    
    save_version = data.get('save_version', '1.0')
    characters = data['characters'] if 'characters' in data else data
    
    return characters

def save_characters(character):
    data = {
        'save_version' : '1.5',
        'characters' : character
    }
    with open(FILE_PATH, 'w') as file:
        json.dump(data, file, indent= 2)