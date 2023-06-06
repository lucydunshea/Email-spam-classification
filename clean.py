import re   # regular expession

class cleaner:  # for cleaning emails ready for NB

    def __init__(self, subject_file):
        self.subject = open(subject_file, 'rt')

    def splitter(self): # Split text file into string of uncleaned words
        for line in self.subject:
            

    def drop_emoji(self):
        for line in self.subject:



