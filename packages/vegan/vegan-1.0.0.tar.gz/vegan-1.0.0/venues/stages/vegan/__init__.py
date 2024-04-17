
'''
	from vegan import build_vegan
	
	vegan = build_vegan ({
		
	})
	
	vegan ["on"] ()
	
	vegan ["retrieve food"] ()
	vegan ["retrieve supp"] ()
	
	vegan ["retrieve recipe"] ()
'''




from vegan._ops.clique import clique

'''

'''
import rich

def build_vegan ():
	def on ():
		return;
	
	return {
		"on": on,
		"off": "",
		
		"retrieve food": "",
		"retrieve supp": "",
		
		"retrieve recipe": ""
	}