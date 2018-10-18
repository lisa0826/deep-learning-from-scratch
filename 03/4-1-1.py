import numpy as np

def mean_squared_error(y, t):
	return 0.5 * np.sum((y-t)**2)

t = [0,0,1,0,0,0,0,0,0,0]
y = [0.1,0.05,0.6,0.0,0.05,0.1,0.0,0.1,0.0,0.0]

# t1 = [0,0,0,0,0,0,0,1,0,0]
y1 = [0.1,0.05,0.1,0.0,0.05,0.1,0.0,0.6,0.0,0.0]

# t2 = [0,0,0,0,0,0,1,0,0,0]
y2 = [0.1,0.05,0.1,0.0,0.05,0.1,0.6,0.1,0.0,0.0]

print(mean_squared_error(np.array(y),np.array(t)))
print(mean_squared_error(np.array(y1),np.array(t)))
print(mean_squared_error(np.array(y2),np.array(t)))

#通过不同情况的测试，理解均方误差