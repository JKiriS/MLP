# -*- coding: utf-8 -*-

import numpy as np

class TfIdf(object):
 	@staticmethod
 	def tfidf(data):
 		data = np.array(data, dtype='float64')
 		N, M = data.shape
 		idf = np.log10(float(N) / np.sum(data!=0, axis=0)) 		
 		tf = data / np.sum(data, axis=1).T
 		return tf * idf


class CorrelationCoefficient(object):
	@staticmethod
 	def correlationcoefficient(data):
 		data = np.array(data, dtype='float64')
 		exp = np.average(data, axis=0)
 		std = np.sqrt(np.sum((data - exp) ** 2, axis=0))
 		tmp = (data - exp) / std
 		return np.dot(tmp.T, tmp)


def test():
	data = [
		[3, 0, 1, 2],
		[0, 2, 5, 0],
		[0, 1, 6, 4]
	]
	# print TfIdf.tfidf(data)
	print CorrelationCoefficient.correlationcoefficient(data)

if __name__ == '__main__':
	test()