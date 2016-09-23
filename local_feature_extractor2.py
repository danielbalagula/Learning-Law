import os
import string
from nltk.corpus import stopwords
from nltk import word_tokenize

import first_paragraph_getter

from sklearn.feature_extraction.text import TfidfVectorizer

party1FilesPath = "./party1_won/"
party2FilesPath = "./party2_won/"

firstParagraphsStopWordsRemoved = getFirstParagraphs(party1FilesPath)

print firstParagraphsStopWordsRemoved[2]