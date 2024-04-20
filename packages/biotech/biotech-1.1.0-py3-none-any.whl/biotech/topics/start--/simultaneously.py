

import biotech.procedures.scan.starter as scan
from biotech.topics.queues.queue_capacity_limiter import queue_capacity_limiter


def now (
	finds,
	module_paths,
	relative_path,
	records,
	
	simultaneous_capacity = 10
):
	def venture (path):
		[ status ] = scan.start (		
			path = path,
			module_paths = module_paths,
			relative_path = relative_path,
			records = records
		)
	
		return status;
	
	proceeds = queue_capacity_limiter (
		capacity = simultaneous_capacity,
	
		items = finds,
		move = venture
	)

	return proceeds;