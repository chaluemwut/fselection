import numpy.numarray as na

from pylab import *

tf = """0,10
1,69
2,114
3,159
4,196
5,238
6,261"""
    
tfidf = """0,17
1,82
2,146
3,199
4,231
5,267"""
        
bns = """0,14
1,53
2,82
3,117
4,140
5,163
6,182
7,196"""
            
gtfidf = """0,21
1,121
2,221
3,20
4,200
5,120
6,500
7,50"""
                
acc2 = """0,2
1,19
2,58
3,71
4,83
5,93
6,107
7,90"""
                    
f1 = """0,10
1,69
2,114
3,158
4,196
5,237
6,90
7,900"""

def get_series(series):
    tags= [x.split(',') for x in series.split('\n')]
    return [[x[1] for x in tags], [x[0] for x in tags]]

#tagspace
f1 = get_series(f1)
acc2= get_series(acc2)
gtfidf = get_series(gtfidf)
bns= get_series(bns)
tfidf= get_series(tfidf)
tf= get_series(tf)
    #error =  [0.3497             , 0.3108]
    
import matplotlib.pyplot as plt
fig = matplotlib.pyplot.figure()

matplotlib.pyplot.plot(f1[1],f1[0], label='f1', linewidth=2)
matplotlib.pyplot.plot(acc2[1],acc2[0], label='acc2', linewidth=2)
matplotlib.pyplot.plot(gtfidf[1],gtfidf[0], label='gtfidf', linewidth=2)
matplotlib.pyplot.plot(bns[1],bns[0], label='bns', linewidth=2)
matplotlib.pyplot.plot(tfidf[1],tfidf[0], label='tfidf', linewidth=2)
matplotlib.pyplot.plot(tf[1],tf[0], label='tf', linewidth=2)
matplotlib.pyplot.legend(('f1','acc2','gtfidf','bns','tfidf','tf'))
ax1 = fig.add_subplot(111)
ax1.set_ylabel('Percent Correct')
ax1.set_xlabel('Feature Vector Size')
matplotlib.pyplot.suptitle("Percent Correct of NB vs Feature Vector Size (20 Classes)", fontsize='20')
#    xlocations = na.array(range(len(data)))+0.5
#    width = 0.5
#    bar(xlocations, data)#, width=width)
#    yticks(range(0, 8))
#    xticks(xlocations+ width/2, labels)
#    xlim(0, xlocations[-1]+width*2)
#    title("Average Ratings on the Training Set")
#    gca().get_xaxis().tick_bottom()
#    gca().get_yaxis().tick_left()
    
show()