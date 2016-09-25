#Current local features:
	# partyMentionsCountWholeDocument: counts the number of times a party was mentioned in a file
	# nGramsFirstParagraph: a list of all n-grams in the first paragraph in a document
	# partyMentionsCountFirstParagraph: counts the number of times a party was mentioned in the first paragraph
	# keyWordsPresence: checks for the presence of keywords in the last sentence of the first paragraph
		# if keyWordsPresence are all false, checks first paragraph
	# firstParagraphPosition: position of last sentence in first paragraph relative to whole document
	# lastSentencePosition: position of last sentence in first paragraph relative to whole document
	# appellee: the party that is appealing

import os

from first_paragraph_getter import getFirstParagraphsStopWordsRemoved
from helpers import *

selfReferenceKeyWords = ["the court ", "this Court", "I ", "we ", "board", "panel", "judgement"]
verdictKeyWords = ["grant", "reverse", "reject", "ordered", "denied", "affirm", "dismiss", "conclude"]
firstParagraphKeyWords = ['appeals']

def getLocalFeaturesInDir(dir):
	#goes through all possible .txt and .json files in a directory to get features
	for filename in os.listdir(dir):
		if filename.endswith('txt'):
			textFile = open(dir + filename, 'r')
			jsonFileName, extension = os.path.splitext(filename)
			jsonFile = open(dir + jsonFileName + '.json', 'r')
			
			features = getLocalFeaturesInDoc(filename, textFile.read().decode("utf8").lower(), jsonFile.read().decode("utf8").lower())
			#outputs features to file
			_fileName, extension = os.path.splitext(filename)
			outputFileName = _fileName + "_features.json"
			outputFile = open(dir+'features/'+outputFileName, "w")
			outputFile.write(features)
			outputFile.close()

def getLocalFeaturesInDoc(originalFilename, textFile, jsonFile):
	#file output format
	fileName, extension = os.path.splitext(originalFilename)

	#extracting text from document
	parties = getPartyNames(jsonFile)
	firstParagraphInfo = getFirstParagraphsStopWordsRemoved(textFile)
	firstParagraph = firstParagraphInfo.get('content')
	if firstParagraph:
		firstParagraphSentences = getSentences(firstParagraph)
		lastSentenceFirstParagraph = ""
		try:
			lastSentenceFirstParagraph = firstParagraphSentences[-1]
		except:
			pass

	#commonly used variables
	fileLength = len(textFile)
	features = {}

	#extracting features from text
	features['party1MentionsWholeDocument'] = textFile.count(parties['party1'])
	features['party2MentionsWholeDocument'] = textFile.count(parties['party2'])
	if firstParagraph:
		features['party1MentionsFirstParagraph'] = firstParagraph.count(parties['party1'])
		features['party2MentionsFirstParagraph'] = firstParagraph.count(parties['party2'])
		features['firstParagraphPosition'] = float(firstParagraphInfo.get('index'))/ fileLength
		features['nGramsFirstParagraph'] = getNGrams(firstParagraph, 2)
		keyWordsPresence = {}
		for verdictWord in verdictKeyWords:
			for selfWord in selfReferenceKeyWords:
				if selfWord in textFile and verdictWord in textFile and abs(textFile.index(selfWord) - textFile.index(verdictWord) < 5):
					keyWordsPresence["_"+verdictWord] = verdictWord in firstParagraph
			keyWordsPresence[verdictWord] = verdictWord in lastSentenceFirstParagraph
		features['keyWordsPresence'] = keyWordsPresence
		for sentence in firstParagraphSentences:
			if parties['party1'] in sentence and 'appeals' in sentence:
				features['appellee'] = 'party1'
				break
			elif parties['party2'] in sentence and 'appeals' in sentence:
				features['appellee'] = 'party2'
				break
	else:
		print "Could not find first paragraph in file " + originalFilename

	return dictToJSON(features)