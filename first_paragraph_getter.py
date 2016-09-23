import os
import string
from nltk import word_tokenize

from helpers import *

def getFirstParagraphsStopWordsRemoved(doc):
	#returns the first paragraph from a text.. tries methods from most to least accurate retrieval
	return getBetweenJudgesAndIntroduction(doc)

def getBetweenJudgesAndIntroduction(doc):
	#gets any text (usually first paragraph) between text in the following format: "Before A, B, C Judges. (GET-THIS-TEXT) I."
	#returns paragraphs with stopwords removed
	firstParagraph = ""
	currentFileContents = doc.lower()
	currentJudgeListLine = 'before' + findBetween(currentFileContents, 'before', 'judges') + 'judges'
	if currentJudgeListLine != "":
		currentFirstParagraph = findBetween(currentFileContents, currentJudgeListLine, 'i.')
		if currentFirstParagraph != "":
			firstParagraph = currentFirstParagraph
	
	punctuationSet = set(string.punctuation)
	removed_punctuation = s = ''.join(ch for ch in firstParagraph if ch not in punctuationSet)
	firstParagraphStopWordsRemoved = removeStopWords(removed_punctuation)
	return firstParagraphStopWordsRemoved
