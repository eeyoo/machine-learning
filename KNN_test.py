import KNN

group, labels = KNN.createDataSet()

for i in range(4):
	print KNN.classify0(group[i],group,labels,3)
	
