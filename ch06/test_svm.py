import svmMLiA
#from numpy import *

#dataArr, labelArr = svmMLiA.loadDataSet('testSet.txt')
#print labelArr, "\n"

#b, alphas = svmMLiA.smoSimple(dataArr, labelArr, 0.6, 0.001, 40)
#print b

#b, alphas = svmMLiA.smoP(dataArr, labelArr, 0.6, 0.001, 20)

#ws = svmMLiA.calcWs(alphas, dataArr, labelArr)
#print ws

#svmMLiA.testRbf()
#svmMLiA.testRbf(2.1)

svmMLiA.testDigits()
svmMLiA.testDigits(('rbf',20))
