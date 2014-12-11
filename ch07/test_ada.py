import adaboost
from numpy import *

datMat,classLabels = adaboost.loadSimpData()

D = mat(ones((5,1))/5)
print D

adaboost.buildStump(datMat,classLabels,D)

