import os
import string
from nltk import word_tokenize

from helpers import *

def getFirstParagraphs(path):
	return getBetweenJudgesAndIntroduction(path)

def getBetweenJudgesAndIntroduction(path):
	#gets any text (usually first paragraph) between text in the following format: "Before A, B, C Judges. (GET-THIS-TEXT) I."
	#returns paragraphs with stopwords removed
	firstParagraphs = []
	for filename in os.listdir(path):
		if filename.endswith('txt'):
			currentFile = open(path + filename, 'r')
			currentFileContents = currentFile.read().lower()
			currentJudgeListLine = 'before' + find_between(currentFileContents, 'before', 'judges') + 'judges'
			if currentJudgeListLine != "":
				currentFirstParagraph = find_between(currentFileContents, currentJudgeListLine, 'i.')
				if currentFirstParagraph != "":
					firstParagraphs.append(currentFirstParagraph.decode("utf8"))
					outputFile = open(path+'first_paragraphs/'+filename+'_FP', 'w')
					outputFile.write(currentFirstParagraph)
	
	firstParagraphsStopWordsRemoved = []
	punctuationSet = set(string.punctuation)
	for firstParagraph in firstParagraphs:
		removed_punctuation = s = ''.join(ch for ch in firstParagraph if ch not in punctuationSet)
		firstParagraphsStopWordsRemoved.append(removeStopWords(removed_punctuation))
	return firstParagraphsStopWordsRemoved
