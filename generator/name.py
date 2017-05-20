import json
from random import choice

FILE_PATH = 'generator/data/names.json'

def generate_name(race, gender):
    with open(FILE_PATH, 'r') as raw:
        data = json.load(raw)

    try:
        return choice(data[race][gender]) + " " + choice(data[race]['othername'])
    except KeyError:
        return None