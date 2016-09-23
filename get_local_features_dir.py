import os

from first_paragraph_getter import getFirstParagraphsStopWordsRemoved
from get_party_names import getPartyNames
from helpers import *

def getLocalFeaturesInDir(dir):
	for filename in os.listdir(dir):
		if filename.endswith('txt'):
			textFile = open(dir + filename, 'r')
			jsonFileName, extension = os.path.splitext(filename)
			jsonFile = open(dir + jsonFileName + '.json', 'r')
			getLocalFeaturesInDoc(filename, textFile.read().decode("utf8").lower(), jsonFile.read().decode("utf8").lower())

def getLocalFeaturesInDoc(originalFilename, textFile, jsonFile):
	fileName, extension = os.path.splitext(originalFilename)
	outputFileName = fileName + "_features.csv"

	firstParagraph = getFirstParagraphsStopWordsRemoved(textFile)
	parties = getPartyNames(jsonFile)
	partyMentionsCount = {'party1': textFile.count(parties['party1']), 'party2': textFile.count(parties['party2'])}
	print fileName
	print parties
	print partyMentionsCount
	print "\n"

def getGlobalFeaturesInDir(dir):
	return
