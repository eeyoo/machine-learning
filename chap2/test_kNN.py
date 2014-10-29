from numpy import *
import matplotlib.pyplot as plt
#from os import listdir

import kNN


##datingDataMat, datingLabels = kNN.file2matrix('datingTestSet2.txt')
##
##fig = plt.figure()
##ax = fig.add_subplot(111)
##ax.scatter(datingDataMat[:,1], datingDataMat[:,2])
##ax.scatter(datingDataMat[:,0], datingDataMat[:,1], 15.0*array(datingLabels),
##	   15.0*array(datingLabels))
##
##plt.xlim(-5000, 100000)
##plt.ylim(-2, 25)
##plt.show()

#kNN.datingClassTest()

#kNN.classifyPerson()

#testVector = kNN.img2vector('testDigits/0_13.txt')
##print testVector[0, 0:31]
##print testVector[0, 32:63]

kNN.handwritingClassTest()
