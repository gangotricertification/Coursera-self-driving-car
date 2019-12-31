import numpy as np
import matplotlib.pyplot as plt

def initiall(w):
	t_data = np.arange(0,20,0.01)

	x = np.zeros_like(t_data)
	y = np.zeros_like(t_data)

	final_x = np.zeros_like(t_data)
	final_y = np.zeros_like(t_data)

	v=np.pi
	xc = 0
	yc = 0
	theta = 0
	delta=0.1974
	t = 1e-2
	beta = 0
	for i in range(t_data.shape[0]):
		beta = np.arctan((1.2*np.tan(delta))/2)
		final_x[i] = xc
		final_y[i] = yc
		xc = xc + v * np.cos(theta+beta)*t
		#print("x",xc)
		yc = yc + v * np.sin(theta+beta)*t
		#print("y",yc)
		theta_d = v*np.cos(beta)*np.tan(delta)/2
		print("theta",theta)
		delta_d = w

		theta = theta + theta_d*t
		delta = delta + delta_d*t

		
	return final_y,final_x
yy,xx=initiall(0)
plt.axis('equal')
plt.plot(xx,yy,label='model created')
plt.legend()
plt.show()
