from datetime import datetime


class Diary:

   




class DiaryEntry:
    def __init__(self):
        self.description = None
        self.created = datetime.now().strftime("%c")
    
    def get_description(self):
        self.description = input('Write your daily diary entry:\n')

    def save(self):
        filename = f'{self.created}.diary'

        with open(filename, 'w') as f:
            f.write(self.description)


