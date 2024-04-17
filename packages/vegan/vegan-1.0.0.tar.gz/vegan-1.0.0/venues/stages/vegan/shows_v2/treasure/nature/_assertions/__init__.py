




'''
	import vegan.shows_v2.treasure.nature._assertions as natures_v2_assertions
	natures_v2_assertions.start (nature)
'''

def are_equal (v1, v2):
	try:
		assert (v1 == v2);
	except Exception as E:
		print ("not equal:", v1, v2)
		raise Exception (E)

	return;


import json
def start (nature):
	assert ("measures" in nature)

	#print (json.dumps (nature, indent = 4))
	
	
	

	return;