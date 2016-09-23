import os
import string

from first_paragraph_getter import getFirstParagraphs
from helpers import *

party1FilesPath = "./party1_won/"
party2FilesPath = "./party2_won/"

party1FirstParagraphsStopWordsRemoved = getFirstParagraphs(party1FilesPath)
party1FirstParagraphsTFIDF = getTFIDF(party1FirstParagraphsStopWordsRemoved)
party1TopTFIDF = dictionarySortByValue(party1FirstParagraphsTFIDF, 10)

party2FirstParagraphsStopWordsRemoved = getFirstParagraphs(party2FilesPath)
party2FirstParagraphsTFIDF = getTFIDF(party2FirstParagraphsStopWordsRemoved)
party2TopTFIDF = dictionarySortByValue(party2FirstParagraphsTFIDF, 10)

for key in party2TopTFIDF:
	if key not in party1TopTFIDF:
		print str(key) + " is not in the party1won corpus"

for key in party1TopTFIDF:
	if key not in party2TopTFIDF:
		print str(key) + " is not in the party2won corpus"