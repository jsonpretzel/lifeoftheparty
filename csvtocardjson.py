import csv
import json

csvFilePath = r'lotp.csv'
jsonFilePath = r'test2.json'

jsonArray = []

with open(csvFilePath) as csvFile:
	csvReader = csv.DictReader(csvFile)

	for rows in csvReader:
		temp = {}
		#print(rows)
		name = rows["name"]
		#print(name)
		temp["count"] = 1
		temp["title"] = name

		#print(rows['quote'])
		if rows["effect"] != "":
			temp["contents"] = ["text | ", "section | Action", "text | " + rows["effect"], "rule", "text | ", " text | " + rows["quote"],  "text | " + " - " + rows["source"], "text | "] 
		else:
			temp["contents"] = ["text | ", "text | " + rows["quote"],  " text | " + " - " + rows["source"], "text | "]
		#data["tags"] = rows["type"]
		print(temp)

		jsonArray.append(temp)
		#print(jsonArray)

with open(jsonFilePath, 'w') as jsonFile:
	jsonFile.write(json.dumps(jsonArray, indent=4))

#print(data)
		#print(jsonFilePath)

