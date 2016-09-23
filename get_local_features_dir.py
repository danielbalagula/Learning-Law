#Current local features:
	# partyMentionsCountWholeDocument: counts the number of times a party was mentioned in a file
	# nGramsFirstParagraph: a list of all n-grams in the first paragraph in a document
	# partyMentionsCountFirstParagraph: counts the number of times a party was mentioned in the first paragraph
	# lastSentenceKeyWords: checks for the presence of keywords in the last sentence of the first paragraph
	# appellee: the party that is appealing

import os

from first_paragraph_getter import getFirstParagraphsStopWordsRemoved
from get_party_names import getPartyNames
from helpers import *

verdictKeyWords = ['affirm', 'reverse', 'reject']
firstParagraphKeyWords = ['appeals']

def getLocalFeaturesInDir(dir):
	#goes through all possible .txt and .json files in a directory to get features
	for filename in os.listdir(dir):
		if filename.endswith('txt'):
			textFile = open(dir + filename, 'r')
			jsonFileName, extension = os.path.splitext(filename)
			jsonFile = open(dir + jsonFileName + '.json', 'r')
			getLocalFeaturesInDoc(filename, textFile.read().decode("utf8").lower(), jsonFile.read().decode("utf8").lower())

def getLocalFeaturesInDoc(originalFilename, textFile, jsonFile):
	#file output format
	fileName, extension = os.path.splitext(originalFilename)
	outputFileName = fileName + "_features.csv"

	#extracting text from document
	parties = getPartyNames(jsonFile)
	firstParagraph = getFirstParagraphsStopWordsRemoved(textFile)
	if firstParagraph:
		firstParagraphSentences = getSentences(firstParagraph)
		lastSentenceFirstParagraph = ""
		try:
			lastSentenceFirstParagraph = firstParagraphSentences[-1]
		except:
			pass

	#extracting features from text
	partyMentionsCountWholeDocument = {'party1': textFile.count(parties['party1']), 'party2': textFile.count(parties['party2'])}
	if firstParagraph:
		nGramsFirstParagraph = getNGrams(firstParagraph, 2)
		partyMentionsCountFirstParagraph = {'party1': firstParagraph.count(parties['party1']), 'party2': firstParagraph.count(parties['party2'])}
		lastSentenceKeyWords = {}
		for keyWord in verdictKeyWords:
			lastSentenceKeyWords[keyWord] = keyWord in lastSentenceFirstParagraph
		appellee = ""
		for sentence in firstParagraphSentences:
			if parties['party1'] in sentence and 'appeals' in sentence:
				appellee = 'party1'
				break
			elif parties['party2'] in sentence and 'appeals' in sentence:
				appellee = 'party2'
				break
		print fileName + " = " + appellee

def getGlobalFeaturesInDir(dir):
	return
