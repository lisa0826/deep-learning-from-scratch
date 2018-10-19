import numpy as np

def numerical_diff(f,x):
	h = 10e-50
	return (f(x+h) - f(x))/h

 print(np.float32(1e-50))