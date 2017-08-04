from numpy import *
import kNN
def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDiffMat**0.5
    sortedDistIndices = distances.argsort()
    classCount = {}
    print '22222'
    print distances
    print '3333'
    print sortedDistIndices
    for i in range(k):
        voteIlabel = labels[sortedDistIndices[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.iteritems(), key = operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

group,labels = kNN.createDataSet()
classify0([0,0], group, labels, 3)