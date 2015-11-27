# -*- coding: utf-8 -*-

import numpy as np

class PageRank(object):
	@staticmethod
	def pagerank(A, d=0.8, eps=0.00001):
		A = np.array(A, dtype='float64')
		N, N = A.shape

		out = np.sum(A, axis=1)
		A[out==0] = np.ones(N, dtype='float64')
		A = A.T / np.sum(A, axis=1)
		
		pr = np.ones((N, 1), dtype='float64') / N
		while True:
			npr = d * np.dot(A, pr) + (1 - d) / N
			if np.max(np.abs(npr - pr)) < eps:
				break
			pr = npr

		return pr

def test():
	A = [
		[0, 1, 0, 0],
		[0, 0, 1, 0],
		[0, 0, 0, 1],
		[1, 0, 0, 0]
	]
	print PageRank.pagerank(A)

if __name__ == '__main__':
	test()