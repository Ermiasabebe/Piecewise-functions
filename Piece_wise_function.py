import numpy as np

import pylab as plt 

def Piecewise(x):

	if x>=2:
	
		return 3*x**2-4
		
	elif x<2:
	
		return 5 + 4*x 
		
	return 0.0
		

def Trig_piece(theta,k):
	if 0 <= theta < np.pi:
		return np.sin(theta)
	elif np.pi/2 <= theta <= np.pi:
		return np.cos(theta +k)
	return 0.0

def exp_piece(x):
	if x<0:
		return x**2 - np.e**x
	elif x>=0:
		return x-1
	return 0.0 
	
def sin_tan(x):
	if x<=np.pi:
		return x*np.sin(x)
	elif x>np.pi:
		return x*np.tan(x)
	return 0.0
	
def sqrt_lin(k, x):
	if 0<=x<=3:
		return np.sqrt(k*x)
	elif 3<x<=10:
		return x+1
	#eturn 0.0


#f __name__ == '__main__':

#ef run_all():
def run_all():

	vecorize_piecewise = np.vectorize(Piecewise)
	x = np.arange(-20,20)
	y=vecorize_piecewise(x)
	plt.plot(x,y) 
	plt.grid()
	plt.show()

	vecorize_trig = np.vectorize(Trig_piece)
	theta= np.linspace(0.1,2*np.pi)
	y = vecorize_trig(theta,np.pi/2)
	plt.plot(theta,y)
	plt.grid()
	plt.show()
	
	vec_exp = np.vectorize(exp_piece)
	x = np.linspace(-20,20)
	y = vec_exp(x)
	plt.plot(x,y)
	plt.grid()
	plt.show()
	
	vec_sintan = np.vectorize(sin_tan)
	x = np.linspace(0.1, 2*np.pi)
	y = vec_sintan(x)
	plt.plot(x,y)
	plt.grid()
	plt.show()
	
	vec_sqrt = np.vectorize(sqrt_lin)
	x =np.linspace(-2,12)
	y = vec_sqrt(2,x)
	plt.plot(x,y)
	plt.grid()
	plt.show()
	
	



