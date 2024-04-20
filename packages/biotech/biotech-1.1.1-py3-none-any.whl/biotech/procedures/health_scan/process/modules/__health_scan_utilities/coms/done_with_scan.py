

'''
	from __coms.done_with_scan import done_with_scan
	done_with_scan ()
'''

from .send_patch import send_patch

def done_with_scan (
	host = "0.0.0.0",
	URL_path = "/done_with_scan",
	port = "",
	
	path = "",
	proceeds = {}
):
	send_patch ("0.0.0.0", port, "/done_with_scan", proceeds)