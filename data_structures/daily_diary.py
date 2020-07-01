# When using the diary app
# the user can save entries to file
# or read the entries by displaying them in the console


import json
from datetime import datetime


class Diary:

    FILENAME = 'diary.json'
    entries = []

    def load(self):
        try:
            with open(self.FILENAME, 'r') as f:
                self.entries = json.loads(f.read())
        except FileNotFoundError:
            return []

    def save(self):
        with open(self.FILENAME, 'w') as f:
            f.write(json.dumps(self.entries))
    
    def add_entry(self, entry):
        self.entries.append(entry.serialize())

    def show_all_entries(self):
        for entry in self.entries:
            description = entry.get('description')
            created = entry.get('created')
            formatted_entry = f'The entry created on {created} is: {description} \n'
            print(formatted_entry)


class Entry:
    def __init__(self):
        self.description = None
        self.created = datetime.now().strftime("%c")
    
    def get_description(self):
        self.description = input('Please enter diary entry:\n')

    def serialize(self):
        return {
            "description": self.description,
            "created": self.created
        }


def main():
    diary = Diary()
    diary.load()

    entry = Entry()
    entry.get_description()
    diary.add_entry(entry)
    diary.save()


if __name__ == "__main__":
    main()
