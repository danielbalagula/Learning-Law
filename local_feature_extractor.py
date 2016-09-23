import os
import string

from get_local_features_dir import getLocalFeaturesInDir

party1FilesDir = "./party1_won/"
party2FilesDir = "./party2_won/"

getLocalFeaturesInDir(party1FilesDir)

# party1FirstParagraphsStopWordsRemoved = getFirstParagraphsStopWordsRemoved(party1FilesPath)
# party2FirstParagraphsStopWordsRemoved = getFirstParagraphsStopWordsRemoved(party2FilesPath)

# print getPartyNames()

# print dictionarySortByValue(getCollectiveNGrams(party2FirstParagraphsStopWordsRemoved), 10, "descending")
# print dictionarySortByValue(getCollectiveNGrams(party1FirstParagraphsStopWordsRemoved), 10, "descending")


# print party2FirstParagraphsTFIDF

# for key in party2TopTFIDF:
# 	if key not in party1TopTFIDF:
# 		print str(key) + " is not in the party1won corpus"

# for key in party1TopTFIDF:
# 	if key not in party2TopTFIDF:
# 		print str(key) + " is not in the party2won corpus"