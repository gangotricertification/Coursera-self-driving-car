import numpy as np
import matplotlib.pyplot as plt 

def longt(throttle,alpha):

	#throttle to engine torque
	a0 = 400
	a1 = 0.1
	a2 = -0.0002

	GR = 0.35   #Gear Ratio
	re = 0.3    #effective radii
	je = 10     #intertia of powertrain
	m = 2000    #mass
	g = 9.81    #gravitational pull

	ca = 1.36   #aerodynamics constraints
	cr1 = 0.01  #friction coefficients

	x = 0       #intitial position
	v = 5       #velocity
	we = 100    #engine angular speed
	t = 50      #time
	acl = 0
	we_dot = 0

	c = 10000
	fmax = 10000          #maximum force by typres

	sample_time = 0.01   #minimum time to test 
	t_data = np.arange(0,t,sample_time)
	x_data = np.zeros_like(t_data)
	v_data = np.zeros_like(t_data)
	throttle = throttle
	
	for i in range(t_data.shape[0]):
		x_data[i] = x
		v_data[i] = v

		ww = GR * we
		s = (ww*re - v)/v    #slip equation

		if (abs(s) < 1):
			fx = c*s
		else:
			fx = fmax

		faero = ca * (v**2)               #aerodynamic force
		frest = cr1 * v                   #resistance force
		fgrav = m * g * np.sin(alpha)     #gravitational force

		fload = faero + frest + fgrav     #net load force

		acl = (fx - fload)/m                                     #calculate acceleration 
		v = v + acl*sample_time                                  #calculate next velocity
		x = x + (2*v - acl*sample_time)/2*sample_time         #calculate next position

		te = throttle * (a0 + (a1*we) + (a2 * we**2))            # torque to engine

		we_dot = (te - GR * re * fload)/je   #angular acceleration
		we = we + we_dot*sample_time           #change in angular speed
	return t_data,v_data


xx,vv = longt(0.2,np.arctan(0/60))   #alpha in negative it mean at declination 
print(xx)
plt.plot(xx,vv)
plt.show()
