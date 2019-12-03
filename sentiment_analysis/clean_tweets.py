##
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint
from bs4 import BeautifulSoup
import re
from nltk.tokenize import WordPunctTokenizer
##

cols = ['sentiment', 'id', 'date', 'query_string', 'user', 'text']
df = pd.read_csv('./data/training.1600000.processed.noemoticon.csv', names=cols, header=None)

df.drop(['id', 'date', 'query_string', 'user'], axis=1, inplace=True)
df['pre_clean_len'] = [len(t) for t in df.text]

##

data_dict = {
    'sentiment': {
        'type': df.sentiment.dtype,
        'description': 'sentiment class - 0:negative, 1:positive'
    },
    'text': {
        'type': df.text.dtype,
        'description': 'tweet text'
    },
    'pre_clean_len': {
        'type': df.pre_clean_len.dtype,
        'description': 'Length of tweet before cleaning'
    },
    'dataset_shape': df.shape
}

##

pattern1 = r'@[A-Za-z0-9_]+' # match @names
pattern2 = r'https?://[^ ]+' # match URLs
pattern3 = r'www.[^ ]+' # match www. URLs
pattern4 = r'[^a-zA-Z]' # match hashtags

negations = {"isn't":"is not", "aren't":"are not", "wasn't":"was not",
             "weren't":"were not","haven't":"have not","hasn't":"has not",
             "hadn't":"had not","won't":"will not", "wouldn't":"would not",
             "don't":"do not", "doesn't":"does not","didn't":"did not",
             "can't":"can not","couldn't":"could not","shouldn't":"should not",
             "mightn't":"might not","mustn't":"must not"}

neg_pattern = re.compile(r'\b(' + '|'.join(negations.keys()) + r')\b')

tok = WordPunctTokenizer()

def tweet_cleaner(text):
    soup = BeautifulSoup(text)

    souped = soup.get_text()
    stripped = re.sub(r'|'.join((pattern1, pattern2)), "", souped)
    stripped = re.sub(pattern3, "", stripped)
    lower_case = stripped.lower()
    neg_handled = neg_pattern.sub(lambda x: negations[x.group()], lower_case)

    letters_only = re.sub(pattern4, " ", neg_handled)

    words = [x for x in tok.tokenize(letters_only) if len(x) > 1]

    return(" ".join(words)).strip()
##

nums = [0,len(df)]
print("Cleaning and parsing the tweets...\n")
clean_tweet_texts = []
for i in range(nums[0],nums[1]):
    if( (i+1)%10000 == 0 ):
        print(f"Tweets {i+1} of {nums[1]} have been processed")
    clean_tweet_texts.append(tweet_cleaner(df['text'][i]))

clean_df = pd.DataFrame(clean_tweet_texts, columns=['text'])
clean_df['target'] = df.sentiment
clean_df.dropna(inplace=True)

clean_df.to_csv('data/clean_tweet.csv', encoding='utf-8')

##
