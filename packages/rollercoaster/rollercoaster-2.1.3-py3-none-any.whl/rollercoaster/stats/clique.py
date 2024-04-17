





def stats_group ():
	import click
	@click.group ("stats")
	def group ():
		pass


	import click
	@group.command ("aggregate_PC_ratio")
	@click.option ('--symbol', required = True)
	def search (symbol):
		print ("symbol:", symbol)
		
		import rollercoaster.climate as climate
		Tradier = climate.find ("Tradier")
		
		import rollercoaster.stats.aggregate_PC_ratio as aggregate_PC_ratio
		import rollercoaster.clouds.Tradier.procedures.options.combine as combine_options  
		PC_ratios = aggregate_PC_ratio.calc ({
			"expirations": combine_options.presently ({
				"symbol": symbol,
				"authorization": Tradier ["authorization"]
			})
		})

		import rich
		rich.print_json (data = {
			"PC ratios": PC_ratios
		})
		
	import click
	@group.command ("aggregate_break_even")
	@click.option ('--symbol', required = True)
	def search (symbol):
		print ("symbol:", symbol)
		
		import rollercoaster.climate as climate
		Tradier = climate.find ("Tradier")
		
		#
		#	This presumes that the symbol is unique...
		#
		import rollercoaster.clouds.Tradier.procedures.options.combine as combine_options  
		import rollercoaster.stats.aggregate_break_even as aggregate_break_even
		break_evens = aggregate_break_even.calc ({
			"expirations": combine_options.presently ({
				"symbol": symbol,
				"authorization": Tradier ["authorization"]
			})
		})

		import rich
		rich.print_json (data = break_evens)
	

	return group




#






