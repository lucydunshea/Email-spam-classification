import re   # regular expession
import string


class Cleaner:  # for cleaning emails ready for NB

    def __init__(self, subject_file):
        self.subject = open(subject_file, 'rt', encoding='utf-8')
        assert self.subject.readline()

    def __enter__(self):    # enter makes object, returns it
        return self

    def splitter(self):     # Split text file into string of uncleaned words
        with self.subject as f:
            text = f.read()
            split_list = text.split()
            return split_list

    def drop_emoji(self, split_list):       # remove emojis and funky characters from a list of words
        emoj = re.compile("["
                          u"\U00002700-\U000027BF"  # Dingbats
                          u"\U0001F600-\U0001F64F"  # Emoticons
                          u"\U00002600-\U000026FF"  # Miscellaneous Symbols
                          u"\U0001F300-\U0001F5FF"  # Miscellaneous Symbols And Pictographs
                          u"\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
                          u"\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
                          u"\U0001F680-\U0001F6FF"  # Transport and Map Symbols
                          "]+", re.UNICODE)
        fixed = []
        for strings in split_list:
            new = re.sub(emoj, '', strings)
            fixed.append(new)
        words_only = [i for i in fixed if i != '']
        return words_only

    def percent(self, words_only):
        percent_to_text = [w.replace('%', 'percent') for w in words_only]
        return percent_to_text

    def de_punc (self, word_list):
        table = str.maketrans('','', string.punctuation)
        stripped = [w.translate(table) for w in word_list]
        return stripped

    def lower_case(self, word_list):
        lower_case = [word.lower() for word in word_list]
        return lower_case

