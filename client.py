import json
import yaml
import nltk
json_data=open('all_data.json')
data = yaml.load(json_data)
di = {} #key is sentence and value is rel array
count = 0
for contrib in data["root"]:
	for element in contrib["data"]:
		
		for x in element:
			#print count
			try:			
				tag_word=element["rels"]
				di[element["sentence"]]=tag_word
			except KeyError:
				continue


print di.keys()
supported_tags_list = ["Price","OS","Org","Phone","Size","Model","Other","Family"]
supported_rel_tags = ["interest_intent","comparison","price_query","feature_query","irrelevant"]



