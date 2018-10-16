import numpy as np

def relu(x):
	return np.maximum(0,x)

A = np.array([[1,2,3],[4,5,6]])
A.shape
B = np.array([[1,2],[3,4],[5,6]])
B.shape
C = np.dot(A,B)
print(C)