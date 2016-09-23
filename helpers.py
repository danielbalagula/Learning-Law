import collections
from itertools import islice
import operator

from nltk.corpus import stopwords
from nltk import word_tokenize

from sklearn.feature_extraction.text import TfidfVectorizer

def removeStopWords(text):
	#removes stop words from a string
	tokens = word_tokenize(text)
	return ' '.join([word for word in tokens if word not in stopwords.words('english')])


def find_between(s, first, last ):
	#Gets text from s between two substrings, first and last
	try:
		start = s.index( first ) + len( first )
		end = s.index( last, start )
		return s[start:end]
	except ValueError:
		return ""

def getTFIDF(docs):
	#gets tf-idf values for words in docs and returns them as a key-value pair of word and score
	tfidf = TfidfVectorizer()
	tfs = tfidf.fit_transform(docs)
	feature_names = tfidf.get_feature_names()
	scores = {}
	for i in range(0, len(feature_names)):
		if (stringHasNumbers(feature_names[i]) == False):
			scores[feature_names[i]] = (tfs[0, i])
	return scores

def dictionarySortByValue(dict, topReturned):
	#sorts a dictionary based on the values
	orderedList = sorted(dict.items(), key=operator.itemgetter(1), reverse=True)
	return orderedList[:topReturned]

def stringHasNumbers(inputString):
	#checks to see if a string has digits in it
	return any(char.isdigit() for char in inputString)