# -*- coding: utf-8 -*-

import numpy as np

def PI(size=3000):
	res = []
	for i in range(1000):
		pts = np.random.rand(size, 2)
		center = np.array([.5, .5])
		dis = np.sqrt(np.sum((pts - center)**2, axis=1))
		res.append(np.sum(dis <= .5) / float(size) * 4)
	return sum(res) / 1000.

def integrate(size=3000):
	res = []
	for i in range(1000):
		pts = np.random.rand(2, size)
		minus = pts[0] - pts[1]**2
		res.append(np.sum(minus <= 0) / float(size))
	return sum(res) / 1000.

def market(size=1000):
	cost = 5.5 + np.random.rand(size) * 2
	status = np.random.randint(0, 3, size)
	cold = np.sum(11 - cost[status==0]) * 5
	hot = np.sum(8 - cost[status==1]) * 10
	warm = np.sum(10 - cost[status==2]) * 7.5
	return (cold + hot + warm) * 10 - 120000
	

if __name__ == '__main__':
	# print PI()
	# print integrate()
	print market()