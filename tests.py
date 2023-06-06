# Keywords: graduate, interview, scholarship, machine learning, Minted New York,
# University of Canterbury, New York City, Running, Training


# training data
train_starred = ['Your activity report','benefits physical activity',
                 'the importance vows']
train_spam = ['send us your password', 'review our website',
              'send your password', 'send us your account']
vocab_words_starred = []
vocab_words_spam = []

def email_cleaner(emails):
    vocab = []
    for sentence in emails:
        sentence_as_list = sentence.split()
        for word in sentence_as_list:
            vocab.append(word)
    vocab_unique = list(dict.fromkeys(vocab))
    return vocab_unique


def spam_level(unique_vocab, train_type):
    dict_spam_level = {}
    for w in unique_vocab:
        emails_with_w = 0       # counter
        for sentence in train_type:
            if w in sentence:
                emails_with_w+=1
        total_spam = len(train_spam)
        spamicity = (emails_with_w+1)/(total_spam+2)
        dict_spam_level[w.lower()] = spamicity
    return dict_spam_level

# def prob_spam(vocab_dict):
