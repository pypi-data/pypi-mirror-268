






import multiply

import os
import time

def check_1 ():

	assert (the_score == 2), the_score

	print ("status 1 pid:", os.getpid ())
	print ("status 1 __file__:", __file__)
	print ("status 1 __name__:", __name__)

	#time.sleep (100)

	return;
	

	
checks = {
	'check 1': check_1
}

