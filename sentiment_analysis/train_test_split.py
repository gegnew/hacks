##
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report, confusion_matrix
from textblob import TextBlob


df = pd.read_csv('data/clean_tweet.csv')
df.drop(columns = 'Unnamed: 0', inplace=True)
##

x = df.text
y = df.target

SEED = 2000

# first split
x_train, x_validation_and_test, y_train, y_validation_and_test = train_test_split(x, y, test_size=0.02, random_state=SEED)

#second split, for train and test data
x_validation, x_test, y_validation, y_test = train_test_split(x_validation_and_test, y_validation_and_test, test_size=0.5, random_state=SEED)
##

# textblob stuff
tbresult = [TextBlob(i).sentiment.polarity for i in x_validation]
tbpred = [0 if n < 0 else 1 for n in tbresult]

conmat = np.array(confusion_matrix(y_validation, tbpred, labels=[1,0]))

confusion = pd.DataFrame(conmat, index=['positive', 'negative'], columns=['predicted_positive', 'predicted_negative'])

# oddly, this has given me very different results that Rick got
# I have a predicted accuracy of 46% and a null accuracy of 77%. This is a bit odd

##
