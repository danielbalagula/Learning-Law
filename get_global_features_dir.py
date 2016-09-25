import os
import json

from helpers import *

combinedNGrams = {}

def getGlobalFeaturesInDir(dir):
	for filename in os.listdir(dir):
		if filename.endswith('json'):
			currentFile = json.loads(open(dir+filename, "r").read())
			try:
				getGlobalNGrams(currentFile['nGramsFirstParagraph'])
			except KeyError:
				pass
	print dictionarySortByValue(combinedNGrams, 20, "descending")

def getGlobalBagOfWords(bow):
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

def getGlobalNGrams(ngrams):
	#gets the counts for all n-grams across documents
	global combinedNGrams
	nGramsAlreadySeen = []
	for nGram in ngrams:
		nGramString = ' '.join(nGram)
		if adequateWord(nGramString) and nGramString not in nGramsAlreadySeen:
			nGramsAlreadySeen.append(nGramString)
			if nGramString not in combinedNGrams :
				combinedNGrams[nGramString] = 1
			else:
				combinedNGrams[nGramString] += 1
	return combinedNGrams