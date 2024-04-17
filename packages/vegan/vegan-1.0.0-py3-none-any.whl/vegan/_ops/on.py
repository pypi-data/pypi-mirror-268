

'''
	import vegan.organisms._regula.on as vegan_on
	vegan_on.on (
		essence_path = "essence.py"
	)
'''

from vegan.organisms.sanique._ops.on import turn_on_sanique
from vegan.organisms.monetary.node.on import turn_on_monetary_node
	
from vegan._essence import retrieve_essence

import rich

def on ():	
	essence = retrieve_essence ()

	rich.print_json (data = essence)

	if ("onsite" in essence ["monetary"]):
		turn_on_monetary_node ()
		
	turn_on_sanique ()	
		
	'''
	sanic_on.on (
		vegan_essence = vegan_essence
	)
	'''