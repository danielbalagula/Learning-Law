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


def findBetween(s, first, last ):
	#Gets text from s between two substrings, first and last
	try:
		start = s.index( first ) + len( first )
		end = s.index( last, start )
		return s[start:end]
	except ValueError:
		return ""

def getGlobalBagOfWords(docs):
	#gets the counts for all bags of words across documents
	bagOfWordsArray = []
	combinedBagOfWords = {}
	for doc in docs:
		currentBOW = []
		for word in doc.split():
			if word not in currentBOW:
				currentBOW.append(word)
		bagOfWordsArray.append(currentBOW)
	for i in range(len(bagOfWordsArray)):
		for word in bagOfWordsArray[i]:
			if word not in combinedBagOfWords and adequateWord(word):
				combinedBagOfWords[word] = 0
				j = i+1
				for j in range(len(bagOfWordsArray)):
					if word in bagOfWordsArray[j]:
						combinedBagOfWords[word] += 1
	return combinedBagOfWords

def getGlobalNGrams(docs):
	#gets the counts for all n-grams across documents
	nGramsArray = []
	combinedNGrams = {}
	for doc in docs:
		currentNGrams = []
		for nGram in find_ngrams(doc.split(),2):
			if nGram not in currentNGrams:
				currentNGrams.append(' '.join(nGram))
		nGramsArray.append(currentNGrams)
	for i in range(len(nGramsArray)):
		for nGram in nGramsArray[i]:
			if nGram not in combinedNGrams and adequateWord(nGram):
				combinedNGrams[nGram] = 0
				j = i+1
				for j in range(len(nGramsArray)):
					if nGram in nGramsArray[j]:
						combinedNGrams[nGram] += 1
	return combinedNGrams

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

def dictionarySortByValue(dict, topReturned, order):
	#sorts a dictionary based on the values
	orderedList = []
	if order == "descending":
		orderedList = sorted(dict.items(), key=operator.itemgetter(1), reverse=True)
	else:
		orderedList = sorted(dict.items(), key=operator.itemgetter(1))
	return orderedList[:topReturned]

def stringHasNumbers(inputString):
	#checks to see if a string has digits in it
	return any(char.isdigit() for char in inputString)

def adequateWord(word):
	#checks to see if the word should be considered for data
	return stringHasNumbers(word) == False and len(word) > 2

def find_ngrams(input_list, n):
	#returns all the n-grams in a string length n
	return zip(*[input_list[i:] for i in range(n)])