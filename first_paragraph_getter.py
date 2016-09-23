import os
import string
from nltk import word_tokenize

from helpers import *

def getFirstParagraphsStopWordsRemoved(doc):
	#returns the first paragraph from a text.. tries methods from most to least accurate retrieval
	doc = doc.lower()
	return getBetweenJudgesAndIntroduction(doc) or getBetweenTwoWords(doc, 'introduction', 'background') or getBetweenOpinionIndent(doc) or getBetweenTwoWords(doc, '', 'i.')

def getBetweenJudgesAndIntroduction(doc):
	#gets any text (usually first paragraph) between text in the following format: "Before A, B, C Judges. (GET-THIS-TEXT) I."
	#returns paragraphs with stopwords removed
	firstParagraph = ""
	currentJudgeListLine = findBetween(doc, 'before', 'judges')
	if currentJudgeListLine != "":
		currentFirstParagraph = findBetween(doc, currentJudgeListLine+'judges.', 'i.')
		if currentFirstParagraph != "":
			firstParagraph = currentFirstParagraph
	
	punctuationSet = set(string.punctuation)
	#removed_punctuation = s = ''.join(ch for ch in firstParagraph if ch not in punctuationSet)
	firstParagraphStopWordsRemoved = removeStopWords(firstParagraph)
	if firstParagraphStopWordsRemoved == "":
		return False 
	else :
		return firstParagraphStopWordsRemoved

def getBetweenTwoWords(doc, first, last):
	#gets any text (usually first paragraph) between text in the following format: "first (GET-THIS-TEXT) last"
	#returns paragraphs with stopwords removed
	firstParagraph = ""
	currentFirstParagraph = findBetween(doc, first, last)
	if currentFirstParagraph != "":
		firstParagraph = currentFirstParagraph
	
	punctuationSet = set(string.punctuation)
	#removed_punctuation = s = ''.join(ch for ch in firstParagraph if ch not in punctuationSet)
	firstParagraphStopWordsRemoved = removeStopWords(firstParagraph)
	if firstParagraphStopWordsRemoved == "":
		return False 
	else :
		return firstParagraphStopWordsRemoved

def getBetweenOpinionIndent(doc):
	firstParagraph = ""
	twoSpacesIndent = findBetween(doc, "opinion", "  ")
	if len(twoSpacesIndent) > 10:
		return twoSpacesIndent
	threeSpacesIndent = findBetween(doc, "opinion", "   ")
	if len(threeSpacesIndent) > 10:
		return twoSpacesIndent
	return False