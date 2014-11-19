'''
	SMO
'''
print __doc__

def loadDataSet(fileName):
	dataMat = []; labelMat = []
	fr = open(fileName)
	for line in fr.readlines():
		lineArr = line.strip().split('\t')
		#dataMat.append(float(lineArr[0]), float(lineArr[1])) # bug
		dataMat.append([float(lineArr[0]), float(lineArr[1])])
		labelMat.append(float(lineArr[2]))
	return dataMat, labelMat

def selectJrand(i, m):
	''' i: index of alpha; m: number of alpha '''
	j = i
	while (j == i):
		j = int(random.uniform(0, m))
	return j

def clipAlpha(aj, H, L):
	if aj > H:
		aj = H
	if L > aj:
		aj = L
	return aj
