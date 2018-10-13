def step_function(x):
	if x > 0:
		return 1
	else:
		return 0
print(step_function(1))


import numpy as np
def step_function(x):
	y = x > 0
	return y.astype(np.int)