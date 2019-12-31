import numpy as np
import matplotlib.pyplot as plt 

def longt():

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
	t = 20      #time

	c = 10000
	fmax = 10000         #maximum force by typres

	sample_time = 0.01   #minimum time to test 
	t_data = np.arange(0,t,sample_time)
	x_data = np.zeros_like(t_data)
	v_data = np.zeros_like(t_data)
	alphat = np.zeros_like(t_data)
	throttle = np.zeros_like(t_data)
	
	for i in range(t_data.shape[0]):
		x_data[i] = x
		v_data[i] = v
		if t_data[i] <= 5.0 :
			throttle[i] = 0.2 + (0.5 - 0.2)*t_data[i]/5
		elif t_data[i] <= 15.0 : 
			throttle[i] = 0.5
		else:
			throttle[i] = 0.5 - (0.5 - 0.0)*(t_data[i]-15)/5

		if x <= 60:
			alpha = np.arctan(3/60)
			alphat[i] = alpha
		elif x <= 150:
			alpha = np.arctan(9/90)
			alphat[i] = alpha
		ww = GR * we
		s = (ww*re - v)/v    #slip equationb

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
		x = x + (v*sample_time + acl*(sample_time**2)/2)         #calculate next position

		te = throttle[i] * (a0 + (a1*we) + (a2 * we**2))            # torque to engine

		we_dot = (te - GR * (re * fload))/je   #angular acceleration
		we = we + we_dot*sample_time           #change in angular speed
	return x_data,v_data,alphat,throttle,t_data
xx,vv,alp,thr,td = longt()   #alpha in negative it mean at declination 

plt.figure(figsize = [8,8])
plt.subplot(221)

plt.plot(td,xx)
plt.xlabel("x (distance)")
plt.ylabel("time")
plt.axvline(x=5, color='r', linestyle='-')
plt.axvline(x=15, color='r', linestyle='-')
plt.axhline(y=60, color='g', linestyle='-')
plt.axhline(y=150, color='g', linestyle='-')

plt.subplot(222)
plt.plot(td,vv)
plt.xlabel("velocity on slope")
plt.ylabel("time")
plt.axvline(x=5, color='r', linestyle='-')
plt.axvline(x=15, color='r', linestyle='-')

plt.subplot(223)
plt.plot(td,alp)
plt.ylabel("time")
plt.xlabel("alpha (inclination angle)")
plt.axvline(x=5, color='r', linestyle='-')
plt.axvline(x=15, color='r', linestyle='-')

plt.subplot(224)
plt.plot(td,thr)
plt.ylabel("time")
plt.xlabel("throttle")
plt.axvline(x=5, color='r', linestyle='-')
plt.axvline(x=15, color='r', linestyle='-')

plt.show()
