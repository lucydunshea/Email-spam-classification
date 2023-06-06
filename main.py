import Algorithms
import datasets
import pandas as pd
import tests
from tqdm import tqdm
import clean

MyMail = 'C:/Users/lucyd/PycharmProjects/ML/venv/Takeout/' \
         'Mail/All mail Including Spam and Trash.mbox'

mbox = datasets.MboxReader(MyMail)

with open('Output_subject.txt', 'w', encoding="utf-8") as file:
    for idx, message in tqdm(enumerate(mbox)):
        # print(message.keys())
        mail_from = f"{str(message['Subject'])}\n".replace('"', '')
        file.write(mail_from)
        #print(idx, message['Subject'])


train_starred = ['Your activity report','benefits physical activity',
                 'the importance vows']
train_spam = ['send us your password', 'review our website',
              'send your password', 'send us your account']
uniques = tests.email_cleaner(train_starred)

star = tests.spam_level(uniques, train_starred)



