
'''
	from vegan.monetary.ingredients.DB.off import turn_off_monetary_node
	mongo_process = turn_off_monetary_node (
		vegan_essence = vegan_essence
	)
'''

'''
	mongod --shutdown --pidfilepath /var/run/mongodb/mongod.pid
'''

import multiprocessing
import subprocess
import time
import os
import atexit

import vegan.mixes.procedure as procedure

def turn_off_monetary_node (
	vegan_essence = {},
	exception_if_off = False
):
	#port = vegan_essence ["monetary"] ["onsite"] ["port"]
	dbpath = vegan_essence ["monetary"] ["onsite"] ["path"]
	PID_path = vegan_essence ["monetary"] ["onsite"] ["PID_path"]
	#logs_path = vegan_essence ["monetary"] ["onsite"] ["logs_path"]
	
	mongo_process = procedure.implicit ([
		"mongod",
		"--shutdown",
		
		'--dbpath', 
		f"{ dbpath }", 
		
		"--pidfilepath",
		f"'{ PID_path }'"
	])
	
	
	
	
	return;