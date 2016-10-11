# -*- coding: utf-8 -*-

import os
import sys
import json

from get_local_features_dir import getLocalFeatureNames
from get_local_features_dir import getVerdictKeyWords
from helpers import *

dir = (sys.argv[1]+'/')

outputFileName = (sys.argv[2])
outputFile = open(outputFileName, 'w')

verdictKeyWords = getVerdictKeyWords()
verdictKeyWords.sort()

for feature in getLocalFeatureNames(): #Sets the local feature labels for the csv file
	if feature == 'keyWordsPresence':
		for keyWord in verdictKeyWords:
			outputFile.write('_'+keyWord+',')
		for keyWord in verdictKeyWords:
			outputFile.write(keyWord+',')
	elif feature != 'nGramsFirstParagraph':
		outputFile.write(feature+',')

globalNgrams = json.loads(open(dir+'globalFeatures.json', 'r').read())['nGrams'] #Sets the global feature labels for the csv file
for globalNgram in globalNgrams:
	outputFile.write(globalNgram[0].encode('utf8')+',')

outputFile.write('\n')

for filename in os.listdir(dir): #Gets the information from the feature files
	if filename.endswith('.json') and filename != 'globalFeatures.json':
		currentDoc = open(dir+filename, 'r').read()
		features = dictionarySortByKey(json.loads(currentDoc))
		for key, value in features.iteritems():
			if (key == 'keyWordsPresence'):
				for keyWord, presence in dictionarySortByKey(value).iteritems():
					outputFile.write(str(presence)+',')
			elif (key != u'nGramsFirstParagraph'):
				outputFile.write(str(value)+',')
		#TBD: use sets
		for globalNgram in globalNgrams:
			currently_found = False	
			try:
				for ngram in features['nGramsFirstParagraph']:
					if ' '.join(ngram) == globalNgram[0]:
						outputFile.write('True,')
						currently_found = True
				if currently_found == False:
					outputFile.write('False,')
			except KeyError:
				pass
	outputFile.write('\n')
outputFile.close()
