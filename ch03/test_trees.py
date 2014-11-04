import trees

myDat, labels = trees.createDataSet()
print myDat
##
##shan = trees.calcShannonEnt(myDat)
##print "\nShannon Entries of myData is %f " % (shan)

print "\n Best feature in myDat: %d" % (trees.chooseBestFeatureToSplit(myDat))

print '\n'
print trees.createTree(myDat, labels)
