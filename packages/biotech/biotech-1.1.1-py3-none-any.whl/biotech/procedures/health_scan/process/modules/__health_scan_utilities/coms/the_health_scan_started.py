

'''
	from __coms.the_health_scan_started import the_health_scan_started
	the_health_scan_started (
		proceeds = {
			"path": ""
		}
	)
'''

from .send_patch import send_patch

def the_health_scan_started (
	host = "0.0.0.0",
	URL_path = "/the_health_scan_started",
	port = "",
	
	path = "",
	proceeds = {}
):
	send_patch ("0.0.0.0", port, "/the_health_scan_started", proceeds)