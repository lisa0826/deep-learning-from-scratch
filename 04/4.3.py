import numpy as np

def numerical_diff(f,x):
	h = 10e-50
	# h1 = 1e-4
	return (f(x+h) - f(x))/h
	# return (f(x+h1) - f(x-h1))/(2*h1)

print(np.float32(1e-50))

