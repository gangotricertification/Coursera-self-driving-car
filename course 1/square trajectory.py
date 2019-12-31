import numpy as np
import matplotlib.pyplot as plt

def initiall():
	t_data = np.arange(0,60,0.01)

	x = np.zeros_like(t_data)
	y = np.zeros_like(t_data)

	final_x = np.zeros_like(t_data)
	final_y = np.zeros_like(t_data)

	w = np.zeros_like(t_data)
	'''
	w[200:200+100]=0.753    #change complete in time from 60 to 20
	w[300:300+100]= -0.753
	
	w[700:700+100]=0.753
	w[800:800+100]= -0.753
	w[1200:1200+100]=0.753
	w[1300:1300+100]=-0.753
	w[1700:1700+100]=0.753
	w[1800:1800+100]=-0.753
	'''
	w[670:670+100] = 0.753
	w[670+100:670+100*2] = -0.753
	w[2210:2210+100] = 0.753
	w[2210+100:2210+100*2] = -0.753
	w[3670:3670+100] = 0.753
	w[3670+100:3670+100*2] = -0.753
	w[5220:5220+100] = 0.753
	w[5220+100:5220+100*2] = -0.753
	
	v = np.zeros_like(t_data)
	v[:] = 4
	xc = 0
	yc = 0
	theta = 0
	delta=0   #delta is 0 as we don't want our trajectory to be
	         # curve at  any angular speed
	t = 1e-2
	beta = 0
	for i in range(t_data.shape[0]):
		beta = np.arctan((1.2*np.tan(delta))/2)
		if w[i] > 0:
			w[i] = min(w[i],1.22)
		else:
			w[i] = max(w[i],-1.22)
		final_x[i] = xc

		final_y[i] = yc
		xc = xc + v[i] * np.cos(theta+beta)*t
		#print("x",xc)
		yc = yc + v[i] * np.sin(theta+beta)*t
		#print("y",yc)
		theta_d = v[i]*np.cos(beta)*np.tan(delta)/2
		#print("theta",theta)
		delta_d = w[i]

		theta = theta + theta_d*t
		delta = delta + delta_d*t
		

		
	return final_y,final_x
yy,xx=initiall()
plt.axis('equal')
plt.plot(xx,yy,label='model created')
plt.legend()
plt.show()
