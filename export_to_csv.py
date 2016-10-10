import os
import sys
import json

from get_local_features_dir import getLocalFeatureNames
from get_local_features_dir import getVerdictKeyWords
from helpers import *

dir = (sys.argv[1]+'/')

outputFileName = 'data.csv'
outputFile = open(outputFileName, 'w')

verdictKeyWords = getVerdictKeyWords()
verdictKeyWords.sort()

for feature in getLocalFeatureNames(): #Sets the labels for the csv file
	if feature == 'keyWordsPresence':
		for keyWord in verdictKeyWords:
			outputFile.write('_'+keyWord+',')
		for keyWord in verdictKeyWords:
			outputFile.write(keyWord+',')
	elif feature != 'nGramsFirstParagraph':
		outputFile.write(feature+',')

outputFile.write('\n')

for filename in os.listdir(dir): #Gets the information from the feature files
	if filename.endswith('.json') and filename != 'globalFeatures.json':
		currentDoc = open(dir+filename, 'r').read()
		features = dictionarySortByKey(json.loads(currentDoc))
		for key, value in features.iteritems():
			if (key == 'keyWordsPresence'):
				for keyWord, presence in dictionarySortByKey(value).iteritems():
					print keyWord
					outputFile.write(str(presence)+',')
			elif (key != u'nGramsFirstParagraph'):
				print key
				outputFile.write(str(value)+',')
	outputFile.write('\n')
outputFile.close()
