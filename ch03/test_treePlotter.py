import treePlotter

#treePlotter.createPlot()


##print treePlotter.retrieveTree(0), '\n'
##print treePlotter.retrieveTree(1)

myTree = treePlotter.retrieveTree (0)
##print treePlotter.getNumLeafs(myTree), '\n'
##print treePlotter.getTreeDepth(myTree)

myTree['no surfacing'][3] = 'maybe'
print myTree

treePlotter.createPlot(myTree)

