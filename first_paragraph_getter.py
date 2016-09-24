# -*- coding: utf-8 -*-

import os
import string
from nltk import word_tokenize

from helpers import *

def getFirstParagraphsStopWordsRemoved(doc):
	#returns the first paragraph from a text.. tries methods from most to least accurate retrieval
	doc = doc.lower()
	return False \
	or getBetweenJudgesAndIntroduction(doc) \
	or getBetweenTwoStrings(doc, 'i.', 'ii.') \
	or getBetweenTwoStrings(doc, '1.', '2.') \
	or getBetweenTwoStrings(doc, '[1].', '[2]') \
	or getBetweenTwoStrings(doc, '¶1', '¶2') \
	or getBetweenTwoStrings(doc, 'introduction', 'background') \
	or getBetweenTwoStrings(doc, 'introduction', 'facts') \
	or getBetweenTwoStrings(doc, 'opinion', 'background') \
	or getBeforeString(doc,'i.') \
	or getBetweenStringAndIndent(doc, 'introduction') \
	or getBeforeString(doc,'background') \
	or getBetweenStringAndIndent(doc, 'opinion') \

def getBetweenJudgesAndIntroduction(doc):
	#gets any text (usually first paragraph) between text in the following format: "Before A, B, C Judges. (GET-THIS-TEXT) I."
	#returns paragraphs with stopwords removed
	firstParagraph = ""
	currentJudgeListLine = findBetween(doc, 'before', 'judges')
	if currentJudgeListLine != "":
		currentFirstParagraph = findBetween(doc, currentJudgeListLine+'judges.', 'i.')
		if currentFirstParagraph != "":
			firstParagraph = currentFirstParagraph	
	firstParagraphStopWordsRemoved = removeStopWords(firstParagraph)
	if firstParagraphStopWordsRemoved == "":
		return False 
	else :
		return {'content': firstParagraphStopWordsRemoved, 'index': doc.index(firstParagraph)+len(firstParagraph)}

def getBetweenTwoStrings(doc, first, last):
	#gets any text (usually first paragraph) between text in the following format: "first (GET-THIS-TEXT) last"
	#returns paragraphs with stopwords removed
	firstParagraph = ""
	currentFirstParagraph = findBetween(doc, first, last)
	if currentFirstParagraph != "":
		firstParagraph = currentFirstParagraph
	firstParagraphStopWordsRemoved = removeStopWords(firstParagraph)
	if firstParagraphStopWordsRemoved == "":
		return False 
	else :
		return {'content': firstParagraphStopWordsRemoved, 'index': doc.index(firstParagraph)+len(firstParagraph)}

def getBetweenStringAndIndent(doc, string):
	#gets any text in the following format "string (GET-THIS-TEXT)   "
	firstParagraph = ""
	firstParagraphStopWordsRemoved = ""
	twoSpacesIndent = findBetween(doc, string, "  ")
	if len(twoSpacesIndent) > 25:
		firstParagraph = twoSpacesIndent
		firstParagraphStopWordsRemoved = removeStopWords(firstParagraph)
	threeSpacesIndent = findBetween(doc, string, "   ")
	if len(threeSpacesIndent) > 25:
		firstParagraph = twoSpacesIndent
		firstParagraphStopWordsRemoved = removeStopWords(firstParagraph)
	return {'content': firstParagraphStopWordsRemoved, 'index': doc.index(firstParagraph)+len(firstParagraph)}

def getBeforeString(doc, string):
	#gets any text in the following format "(GET-THIS-TEXT) string"
	currentFirstParagraph = findBetween(doc, "", string)
	firstParagraphStopWordsRemoved = removeStopWords(currentFirstParagraph)
	if firstParagraphStopWordsRemoved == "":
		return False 
	else :
		return {'content': firstParagraphStopWordsRemoved, 'index': doc.index(firstParagraph)+len(firstParagraph)}