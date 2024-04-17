

'''
	import rollercoaster.gadgets.clock.UTC.current as UTC_current
	current_time = UTC_current.discover ()
'''

from datetime import datetime

def discover ():
	current_UTC_time = datetime.utcnow ()
	formatted_UTC_time = current_UTC_time.strftime ("%Y-%m-%d %H:%M:%S")

	print ("Formatted UTC time:", formatted_UTC_time)
	
	return formatted_UTC_time
