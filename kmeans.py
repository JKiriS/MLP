# -*- coding: utf-8 -*-

import numpy as np

class KMeans(object):
	@staticmethod
	def kmeans(data, K=3, centers=None, eps=0.000001):
		data = np.array(data, dtype='float64')
		N, M = data.shape
		
		if not centers:
			centers = data[np.random.choice(N, K, replace=False)]
		
		while True:	
			# calculate distance to each center 
			dis = np.array([np.sum((data - centers[i]) ** 2, axis=1) \
				for i in range(K)], dtype='float64').T 
			# update cluster label
			clusters = np.argmin(dis, axis=1)
			# update centers
			new_centers = np.array([np.average(data[clusters==i], axis=0) \
				for i in range(K)], dtype='float64')
			# if converged
			if np.max(np.abs(centers - new_centers)) < eps:
				break
			centers = new_centers

		return clusters, centers

def test():
	data = [
		[3, 0, 1, 2],
		[0, 2, 5, 0],
		[0, 1, 6, 4],
		[1, 1, 5, 5]
	]
	print KMeans.kmeans(data)

if __name__ == '__main__':
	test()