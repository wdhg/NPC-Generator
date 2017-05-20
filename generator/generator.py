import json
from random import choice

DATA_FILE_PATH = 'generator/data/data.json'

class Generator(object):
    def __init__(self):
        with open(DATA_FILE_PATH, 'r') as raw:
            self.data = json.load(raw)

    def generate(self, race=None, gender=None, moral=None, ethic=None):
        if race == None:
            race = choice(self.data['races'])
        if gender == None:
            gender = choice(self.data['genders'])
        if race not in self.data['races'] or gender not in self.data['genders']:
            return None

        if moral == None:
            moral = choice(self.data['morals'])
        if ethic == None:
            ethic = choice(self.data['ethics'])

        return {
            'race': race,
            'gender': gender,
            'alignment': [moral, ethic],
            'name': [
                choice(self.data['names'][race][gender]),
                choice(self.data['names'][race]['othername'])
            ],
            'apperance': choice(self.data['apperances']),
            'abilities': None,
            'talent': choice(self.data['talents']),
            'mannerism': choice(self.data['mannerisms']),
            'interaction_trait': choice(self.data['interactionTraits']),
            'ideal': [
                choice(self.data['ideals'][moral]),
                choice(self.data['ideals'][ethic])
            ],
            'bond': choice(self.data['bonds']),
            'flaw': choice(self.data['flaws']),
        }