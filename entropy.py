# -*- coding: utf-8 -*-

import numpy as np

class Entropy(object):
	@staticmethod
	def entropy(x):
		N = x.shape[0]
		values = set(x)
		h = 0
		for v in values:
			vp = np.sum(x==v) / float(N)
			h -= vp * np.log2(vp)
		return h

	@staticmethod
	def entropyXY(x, y):
		N = x.shape[0]
		valuesx = set(x)
		valuesy = set(y)
		h = 0
		for vx in valuesx:
			for vy in valuesy:
				vp = np.sum((x==vx)&(y==vy)) / float(N)
				if vp > 0:
					h -= vp * np.log2(vp)
		return h

	@staticmethod
	def mutualEntropy(x, y):
		return Entropy.entropy(x) + Entropy.entropy(y) - Entropy.entropyXY(x, y)

def test():
	data = [
		[0, 0],
		[0, 0],
		[0, 1],
		[0, 1],
		[0, 0],
		[1, 0],
		[1, 0],
		[1, 1],
		[1, 1],
		[1, 1],
		[2, 1],
		[2, 1],
		[2, 1],
		[2, 1],
		[2, 0],
	]
	data = np.array(data)
	print Entropy.entropy(data[:,0])
	print Entropy.entropy(data[:,1])
	print Entropy.entropyXY(data[:,0], data[:,1])
	print Entropy.mutualEntropy(data[:,0], data[:,1])

if __name__ == '__main__':
	test()