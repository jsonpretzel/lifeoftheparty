# This script converts .csv files into a .json file for use in rpg-cards to generate cards for Life Of The Party.  
# https://jsonpretzel.itch.io/life-of-the-party
# The below script uses text formatting functions created specifically for the lotp branch (https://github.com/jsonpretzel/rpg-cards/tree/lotp), 
# but alternatively, bold and italic text can be added to the scripts below using "<b>" + ____ + "</b>" in the lotp or Master branch versions.

import csv
import json

csvFilePath = r'lotp-final.csv'  # your input .csv file
jsonFilePath = r'lotp-final-gj.json'  # name of output .json file to upload to rpg-cards

jsonArray = [] # array storing data from each .csv row to be converted to separate .json 

with open(csvFilePath, encoding='utf-8') as csvFile: # open and read the input .csv file
	csvReader = csv.DictReader(csvFile)

	for rows in csvReader:
		temp = {} # dictionary to store relevant .csv info
		name = rows["name"]
		temp["count"] = 1
		temp["title"] = name

		# check if a row had information under the "effect" column. If so, check for effect_type, and generate Scenario card dictionary accordingly
		if rows["effect"] != "":
			if rows["effect_type"] == "immediate":
				temp["contents"] = ["text | ", "section | <b>Scenario (Immediate)</b>", "text | " + rows["effect"], "rule", "text | ", " italic | " + rows["quote"], "text | ", "italicbold | " + " - " + rows["source"], "text | "] 
			elif rows["effect_type"] == "linger":
				temp["contents"] = ["text | ", "section | <b>Scenario (Lingering)</b>", "text | " + rows["effect"], "rule", "text | ", " italic | " + rows["quote"], "text | ",  "italicbold | " + " - " + rows["source"], "text | "] 
		# if no "effect" column, generate Guest card dictionary instead 
        else:
			temp["contents"] = ["text | ", "section | <b>Guest</b>","text | ", "text | ", "italic | " + rows["quote"], "text | ", " italicbold | " + " - " + rows["source"], "text | "]
		
		print(temp) # optional, but prints data to be committed
        
		jsonArray.append(temp) # add the card dictonary as a new element in an array holding every card dictontary to convert to .json

# write every storied card Dictionary array into the output .json file, ready to be uploaded into rpg-cards
with open(jsonFilePath, 'w') as jsonFile:
	jsonFile.write(json.dumps(jsonArray, indent=4))
