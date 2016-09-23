from helpers import *
import json

def getPartyNames(doc):
	#Does not account for parties being referred to by their position, such as common in the case of Secretary
	parsed_json = json.loads(doc)
	caseNameString = "STARTNAME" + parsed_json['citation']['case_name'] + "ENDNAME"
	parties = {}
	if "v." in caseNameString:
		parties['party1'] = findBetween(caseNameString, "STARTNAME", "v.")
		parties['party2'] = findBetween(caseNameString, "v.", "ENDNAME")
	return parties