import numpy
import random
import pylab

def plothisty(listy,xoxo,yoyo,title):
    bins = [0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550]
    pylab.hist(listy, bins)
    pylab.xlabel(xoxo)
    pylab.ylabel(yoyo)
    pylab.title(title, fontsize=14,fontweight='bold')
    pylab.show()