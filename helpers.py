import collections
import json
import operator
import string
from itertools import islice

from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktParameters

from sklearn.feature_extraction.text import TfidfVectorizer

def getPartyNames(doc):
	#Does not account for parties being referred to by their position, such as common in the case of Secretary
	parsed_json = json.loads(doc)
	caseNameString = "STARTNAME" + parsed_json['citation']['case_name'] + "ENDNAME"
	parties = {}
	if "v." in caseNameString:
		parties['party1'] = findBetween(caseNameString, "STARTNAME", "v.")
		parties['party2'] = findBetween(caseNameString, "v.", "ENDNAME")
	return parties

def removeStopWords(tokens):
	#removes stop words from a string
	return ' '.join([word for word in tokens if word not in stopwords.words('english')])

def wordTokenize(text):
	return word_tokenize(text)


def findBetween(s, first, last ):
	#Gets text from s between two substrings, first and last
	try:
		start = s.index( first ) + len( first )
		end = s.index( last, start )
		return s[start:end]
	except ValueError:
		return ""

def getTFIDF(docs, topAmount):
	#gets tf-idf values for words in docs and returns them as a key-value pair of word and score
	tfidf = TfidfVectorizer()
	tfs = tfidf.fit_transform(docs)
	feature_names = tfidf.get_feature_names()
	scores = {}
	for i in range(0, len(feature_names)):
		if (stringHasNumbers(feature_names[i]) == False):
			scores[feature_names[i]] = (tfs[0, i])
	return scores.sort(reverse=True)[topAmount]

def dictionarySortByValue(dict, topReturned, order):
	#sorts a dictionary based on the values
	orderedList = []
	if order == "descending":
		orderedList = sorted(dict.items(), key=operator.itemgetter(1), reverse=True)
	else:
		orderedList = sorted(dict.items(), key=operator.itemgetter(1))
	return orderedList[:topReturned]

def dictionarySortByKey(dict):
	return collections.OrderedDict(sorted(dict.items()))

def stringHasNumbers(inputString):
	#checks to see if a string has digits in it
	return any(char.isdigit() for char in inputString)

def adequateWord(word):
	#checks to see if the word should be considered for data
	return stringHasNumbers(word) == False and len(word) > 2

def getNGrams(text, n):
	#returns all the n-grams in a string length n
	input_list = word_tokenize(removePunctuation(text))
	return zip(*[input_list[i:] for i in range(n)])

def removePunctuation(text):
	punctuationSet = set(string.punctuation)
	outputString = ''
	ignoreAfterApostrophe = False
	for ch in text:
		if ch == '\'':
			ignoreAfterApostrophe = True
		elif ignoreAfterApostrophe:
			ignoreAfterApostrophe = False
		elif ch not in punctuationSet:
			outputString += ch
	return outputString

def getSentences(text):
	#returns a list of sentences tokenized by Punkt
	punkt_param = PunktParameters()
	punkt_param.abbrev_types = set(['dr', 'vs', 'mr', 'mrs', 'prof', 'inc'])
	sentence_splitter = PunktSentenceTokenizer(punkt_param)
	sentences = sentence_splitter.tokenize(text)
	return sentences

def dictToJSON(dict):
	return json.dumps(dict, ensure_ascii=True)