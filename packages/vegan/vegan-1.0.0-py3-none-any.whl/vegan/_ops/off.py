

'''
	import vegan._interfaces.off as vegan_off
	vegan_off.off (
		essence_path = "essence.py"
	)
'''

import vegan.monetary.off as monetary_off
import vegan._interfaces.sanique.off as sanic_off

from vegan._essence import prepare_essence
from vegan._essence import run_script_from_file

def off (
	essence_path
):	
	vegan_essence = prepare_essence (
		run_script_from_file (essence_path)
	)
	if ("onsite" in vegan_essence ["monetary"]):
		mongo_process = monetary_off.off (
			vegan_essence = vegan_essence
		)
	
	sanic_off.off (
		vegan_essence = vegan_essence
	)
	
	