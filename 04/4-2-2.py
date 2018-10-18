import numpy as np

#把变量变为默认参数，这样如果别人使用我的函数时，不需要固定的参数，可以直接覆盖，不传值就为默认值，关于函数的参数讲解，见4-2-2.txt
def cross_entropy_error(y,t,delta= 1e-7):
	return -np.sum(t * np.log(y + delta))

t = [0,0,1,0,0,0,0,0,0,0]
y = [0.1,0.05,0.6,0.0,0.05,0.1,0.0,0.1,0.0,0.0]

y1 = [0.1,0.05,0.1,0.0,0.05,0.1,0.0,0.6,0.0,0.0]

print(cross_entropy_error(np.array(y),np.array(t)))
print(cross_entropy_error(np.array(y1),np.array(t)))


