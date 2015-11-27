# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

class DBSCAN(object):
	'''
		This cluster algorithm is based on https://en.wikipedia.org/wiki/DBSCAN
	'''
	def __init__(self, eps, MinPts):
		self.eps = eps
		self.MinPts = MinPts
		self.data = None
		self.N = 0
		self.clusters = None
		self.visited = None

	@staticmethod
	def regionQuery(data, pt, eps):
		N = data.shape[0]
		return np.arange(N)[np.linalg.norm(data-pt, axis=1) < eps]

	def expandCluster(self, NeighborPts, C):
		if self.data is None:
			raise Exception('No Data')
		j = 0
		while j < NeighborPts.shape[0]:
			i = NeighborPts[j]
			if self.visited[i] == 0:
				self.visited[i] = 1
				neighbors = DBSCAN.regionQuery(self.data, self.data[i], self.eps)
				if neighbors.shape[0] >= self.MinPts:
					NeighborPts = np.hstack([NeighborPts, neighbors])
			if self.clusters[i] == 0:
				self.clusters[i] = C
			j += 1

	def cluster(self, data):
		self.data = data
		self.N = data.shape[0]
		self.clusters = np.zeros(self.N)
		self.visited = np.zeros(self.N)

		C = 0
		for i in np.arange(self.N):
			if self.visited[i] == 1:
				continue
			self.visited[i] = 1
			NeighborPts = DBSCAN.regionQuery(data, data[i], self.eps)
			if NeighborPts.shape[0] < self.MinPts:
				self.clusters[i] = -1
			else:
				C += 1
				self.clusters[i] = C
				self.expandCluster(NeighborPts, C)
		return self.clusters


def genData():
	n = 500

	r1 = np.random.normal(10, 1, n)
	theta1 = np.random.rand(n) * np.pi
	data1 = np.vstack([r1*np.cos(theta1), r1*np.sin(theta1)]).T

	r2 = np.random.normal(4, 1, n)
	theta2 = np.random.rand(n) * np.pi
	data2 = np.vstack([r2*np.cos(theta2), r2*np.sin(theta2)]).T

	return np.vstack([data1, data2])


def test():
	data = genData()
	model = DBSCAN(1, 8)
	clusters = model.cluster(data)

	colors = ['red', 'green', 'blue']

	plt.scatter(data[clusters==-1][:,0], data[clusters==-1][:,1], c='gray', edgecolors='none')
	for i, c in enumerate(colors):
		plt.scatter(data[clusters==i+1][:,0], data[clusters==i+1][:,1], c=c, edgecolors='none')
	plt.show()


if __name__ == '__main__':
	test()