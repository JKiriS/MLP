# -*- coding: utf-8 -*-

data = [
		[1, 3, 4],
		[2, 3, 5],
		[1, 2, 3, 5],
		[2, 5]
	]

def createC1(ds):
	C1 = reduce(lambda a, b:a | b, map(set, ds), set([]))
	return map(lambda a:frozenset([a]), C1)

def checkSupport(D, Ck, minSupport):
	ssCnt = {}
	for transaction in D:
		for can in Ck:
			if can.issubset(transaction):
				ssCnt[can] = ssCnt.get(can, 0) + 1
	numItems = float(len(D))
	res = []
	for can in ssCnt:
		support = ssCnt[can] / numItems
		if support >= minSupport:
			res.append((can, support))
	return dict(res)
# print checkSupport(map(set, data), createC1(data), .5).keys()

def genCk(Lk):
	Ck = []
	if len(Lk) == 0:
		return Ck
	k = len(Lk[0]) + 1
	for i in range(len(Lk)):
		for j in range(i+1, len(Lk)):
			L1 = list(Lk[i])[:k-2]; L2 = list(Lk[j])[:k-2]
			L1.sort(); L2.sort()
			if L1 == L2:
				Ck.append(Lk[i] | Lk[j])
	return Ck
# print genCk(createC1(data))

def apriori(ds, minSupport):
	C1 = createC1(ds)
	D = map(set, data)
	supData = checkSupport(D, C1, minSupport)
	L = [supData.keys()]
	while True:
		if len(L[-1]) <= 1:
			break
		Ck = genCk(L[-1])
		supK = checkSupport(D, Ck, minSupport)
		if len(supK) == 0:
			break
		supData.update(supK)
		L.append(supK.keys())
	return L, supData
# print apriori(data, .7)