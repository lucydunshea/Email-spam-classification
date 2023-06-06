import re   # regular expession

class cleaner:  # for cleaning emails ready for NB

    def __init__(self, subject_file):
        self.subject = open(subject_file, 'rt')

    def splitter(self): # Split text file into string of uncleaned words
        for line in self.subject:
            words = line.split()
            return words

    #def drop_emoji(self):
      #  for line in self.subject:

   # def unique_words(self):
    #   vocab = []
     #   for sentence in emails:
       #     sentence_as_list = sentence.split()
         #   for word in sentence_as_list:
         #       vocab.append(word)
      #  vocab_unique = list(dict.fromkeys(vocab))
       # return vocab_unique

