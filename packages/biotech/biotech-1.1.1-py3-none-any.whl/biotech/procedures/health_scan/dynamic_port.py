
#from biotech.topics.process_on.p_expect import process_on
from biotech.topics.process_on.p_expect.implicit import process_on_implicit

def dynamic_port (
	process_path = "",
	
	env = "",
	name = ""
):
	the_health_check = process_on_implicit (
		"python3 " + process_path,
		
		#CWD = CWD,
		env = env,
		name = name
	)
	
	return the_health_check