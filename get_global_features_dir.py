import os
import json

from helpers import *

combinedNGrams = {}
outputFileName = "globalFeatures.json"
globalFeatures = {}

def getGlobalFeaturesInDir(dir):
	for filename in os.listdir(dir):
		if filename.endswith('json'):
			currentFile = json.loads(open(dir+filename, "r").read())
			try:
				getGlobalNGrams(currentFile['nGramsFirstParagraph'])
			except KeyError:
				pass
	globalFeatures['nGrams'] = dictionarySortByValue(combinedNGrams, 10, "descending")
	print globalFeatures['nGrams']
	outputFile = open(dir+outputFileName, "w")
	outputFile.write(dictToJSON(globalFeatures))
	outputFile.close()

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