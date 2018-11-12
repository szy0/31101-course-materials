import numpy as np
import matplotlib.pyplot as plt

def CreateMap(n):
	roundmap = np.random.rand(n,2)-0.5
	return roundmap

def GenerateRoute(roundmap):
	n = np.size(roundmap,0)
	route = np.zeros(n,dtype = int)
	for i in range(n):
		pointisnew = False
		while not pointisnew:
			trialpoint = np.random.randint(low=0,high=n)
			pointisnew = True
			for  j in range(i):
				if trialpoint == route[j]:
					pointisnew = False
		
		route[i] = trialpoint
	return route

def PlotRoute(roundmap,route):
	routep = np.zeros(np.size(route,0)+1,dtype=int)
	routep[:np.size(route,0)]=route[:] #the last element in routep is 0 for now
	routep[-1] = route[0] #the last element in routep is the starting point 
	plt.axes().set_aspect('equal')
	axes = plt.gca()
	axes.set_xlim([-0.5,0.5])
	axes.set_ylim([-0.5,0.5])
	plt.plot(roundmap[routep[:],0],roundmap[routep[:],1],'b--')
	plt.show()
	
def RouteLength(roundmap,route):
	n = np.size(roundmap,0)
	norm = n*np.sin(np.pi/n)
	distance = 0
	for i in range(n-1):
		distance += np.linalg.norm(roundmap[route[i+1]]-roundmap[route[i]])
	distance += np.linalg.norm(roundmap[route[0]]-roundmap[route[n-1]]) # or route[n-1]
	return distance/norm
	
	

#random search algorithm

n = 10
MyMap = CreateMap(n)
nattempts = 10000
minlengths=[]
minlength = 99999

for i in range(nattempts):
	MyRoute=GenerateRoute(MyMap)
	thislength=routelength(MyMap,MyRoute)
	if (thislength < minlength):
		minlength = thislength
		bestroute = myroute.copy()
		
	minlengths.append(minlength)
MyRoute = GenerateRoute(MyMap)
PlotRoute(MyMap,MyRoute)
print(RouteLength(MyMap,MyRoute))













































