

'''
import euphoria.monetary.ingredients.DB.on as ingredient_DB_on
import euphoria.monetary.ingredients.DB.off as ingredient_DB_off
import euphoria.monetary.ingredients.DB.status as ingredient_DB_status
import euphoria.monetary.ingredients.DB.connect as connect_to_ingredient

'''

#
#	local node toggle
#
from .node.implicit.on import turn_on_monetary_node
from .node.implicit.off import turn_off_monetary_node
#
#	local or remote 
#
from .status import find_monetary_status
from .connect import DB as connect_to_ingredient_DB

from .memories._clique import monetary_memories_clique

from euphoria._essence import prepare_essence

import click

def clique ():
	@click.group ("monetary")
	def group ():
		pass


	@group.command ("on")
	#@click.option ('--example-option', required = True)
	def on ():
		print ("on")
		mongo_process = turn_on_monetary_node (
			euphoria_essence = prepare_essence ({
				"monetary": {}
			})
		)

	@group.command ("off")
	#@click.option ('--example-option', required = True)
	def off ():
		turn_off_monetary_node (
			euphoria_essence = prepare_essence ({
				"monetary": {}
			})
		)

	@group.command ("status")
	#@click.option ('--example-option', required = True)
	def off ():
		find_monetary_status (
			euphoria_essence = prepare_essence ({
				"monetary": {}
			}),
			loop_limit = 3
		)


	group.add_command (monetary_memories_clique ())

	return group




#



