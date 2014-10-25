import KNN
from numpy import *
import matplotlib
import matplotlib.pyplot as plt

datingDataMat, datingLabels = KNN.file2matrix('datingTestSet2.txt')

#print datingDataMat

#print datingLabels


fig = plt.figure()
ax = fig.add_subplot(211)
bx = fig.add_subplot(212)
ax.scatter(datingDataMat[:,1], datingDataMat[:,2])

bx.scatter(datingDataMat[:,1], datingDataMat[:,2],
	   15.0*array(datingLabels), 15.0*array(datingLabels))
plt.show()
