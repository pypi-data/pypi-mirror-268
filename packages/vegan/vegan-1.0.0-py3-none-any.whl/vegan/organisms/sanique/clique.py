

'''
	This is for starting sanique in floating (or implicit) mode.
'''


import vegan._interfaces.sanique.on as sanic_on
import vegan._interfaces.sanique.off as sanic_off
import vegan._interfaces.sanique.status as sanic_status

from vegan._essence import prepare_essence
from vegan._essence import run_script_from_file
	
import click
import rich

import time
import os
import pathlib
from os.path import dirname, join, normpath
import sys

def clique ():

	@click.group ("sanique")
	def group ():
		pass


	@group.command ("on")
	@click.option (
		'--essence-path', 
		default = 'essence.py',
		help = 'vegan sanique on --essence-path essence.py', 
		required = False
	)
	def on (essence_path):			
		essence_full_path = str (normpath (join (os.getcwd (), "essence")))
		vegan_essence = prepare_essence (run_script_from_file (essence_path))
		
		sanic_on.on (
			vegan_essence = vegan_essence
		)
		
		time.sleep (1)
		

	@group.command ("off")
	@click.option (
		'--essence-path', 
		default = 'essence.py',
		help = 'vegan sanique on --essence-path essence.py', 
		required = False
	)
	def off (essence_path):
		essence_full_path = str (normpath (join (os.getcwd (), "essence")))
		vegan_essence = prepare_essence (run_script_from_file (essence_path))
		rich.print_json (data = {
			"vegan_essence": vegan_essence
		})
		sanic_off.off (
			vegan_essence = vegan_essence
		)
		
		time.sleep (1)
		
		
	@group.command ("status")
	@click.option (
		'--essence-path', 
		default = 'essence.py',
		help = 'vegan sanique on --essence-path essence.py', 
		required = False
	)
	def status (essence_path):
		essence_full_path = str (normpath (join (os.getcwd (), "essence")))
		vegan_essence = prepare_essence (run_script_from_file (essence_path))
		rich.print_json (data = {
			"vegan_essence": vegan_essence
		})
		
		sanic_status.status (
			vegan_essence = vegan_essence
		)
		
		time.sleep (1)

	return group




#



