

'''
	import vegan._interfaces.status as vegan_status
	vegan_status.status (
		essence_path = "essence.py"
	)
'''

import vegan.monetary.status as monetary_status
import vegan._interfaces.sanique.status as sanic_status

from vegan._essence import prepare_essence
from vegan._essence import run_script_from_file

import rich

def status (
	essence_path
):	
	vegan_essence = prepare_essence (
		run_script_from_file (
			essence_path
		)
	)

	if ("onsite" in vegan_essence ["monetary"]):
		local_mongo_status = monetary_status.status (
			vegan_essence = vegan_essence
		)
		
	the_sanic_status = sanic_status.status (
		vegan_essence = vegan_essence
	)
	
	the_status = {
		"monetary": {
			"local": local_mongo_status
		},
		"sanique": {
			"local": the_sanic_status
		}
	}
	
	print ()
	rich.print_json (data = {
		"status": the_status
	})
	
	return the_status