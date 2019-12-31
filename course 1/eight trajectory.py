import numpy as np
import matplotlib.pyplot as plt 

def track(w):
	t_data = np.arange(0,30,0.01)

	x = np.zeros_like(t_data)
	y = np.zeros_like(t_data)

	final_x = np.zeros_like(t_data)
	final_y = np.zeros_like(t_data)

	#w = np.arctan(1/4)

	v = 16*np.pi/15

	xc = 0
	yc = 0
	theta = 0
	delta = np.arctan(1/4)
	t = 1e-2
	beta = 0
	for i in range(t_data.shape[0]):
		beta = np.arctan((1.2*np.tan(delta))/2)
		final_x[i] = xc
		final_y[i] = yc
		if i<t_data.shape[0]/8:
			xc = xc + v*np.cos(theta + beta) * t
			yc = yc + v*np.sin(theta + beta) * t

			theta_d = v*np.cos(beta)*np.tan(delta)/2
			delta_d = w

			theta = theta + theta_d*t
			delta = delta + delta_d*t
		elif i<(t_data.shape[0]/8) * 5:
			xc = xc + v*np.cos(theta + beta) * t
			yc = yc + v*np.sin(theta + beta) * t

			theta_d = v*np.cos(beta)*np.tan(np.pi-delta)/2
			delta_d = -w

			theta = theta + theta_d*t
			delta = delta + delta_d*t
		else:
			xc = xc + v*np.cos(theta + beta) * t
			yc = yc + v*np.sin(theta + beta) * t

			theta_d = v*np.cos(beta)*np.tan(delta)/2
			delta_d = w

			theta = theta + theta_d*t
			delta = delta + delta_d*t

	return final_x,final_y

xx,yy = track(0)
plt.axis('equal')
plt.plot(xx,yy,label='model created')
plt.legend()
plt.show()