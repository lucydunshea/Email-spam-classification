import re   # regular expession

class cleaner:  # for cleaning emails ready for ML

    def __init__(self, subject_file):
        self.subject = open(subject_file, 'rt')

    def splitter(self):


    def drop_emoji(self):
        for line in self.subject:



