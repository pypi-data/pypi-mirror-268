



def unlimited_queue (
	venture,
	finds
):
	proceeds = []

	with ThreadPoolExecutor () as executor:
		revenues = executor.map (
			venture, 
			finds
		)
		
		executor.shutdown (wait = True)
		
		for revenue in revenues:
			proceeds.append (revenue)
			
	return proceeds;