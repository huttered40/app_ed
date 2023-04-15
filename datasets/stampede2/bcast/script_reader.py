# Goal is simply o shuffle the dataset so that it is not stacked in order of (ppn,nnodes)

import numpy as np


# Must randomize when selecting a test set from this dataset because the data had been entered one (ppn) at a time
fp = open('kt2.csv','r')
fpw = open('kt2_train.csv','w')
lines = fp.readlines()
#fpw.write(lines[0])

# Apparently cannot shuffle if the list is accessed as [1:] upon argument, so I temporarily removed the header
np.random.shuffle(lines)

for line in lines:
    x = line.split(',')
    if (int(x[2]) != 1 or int(x[3]) != 1):
        fpw.write('%s,%s,%s,%s,%s,%s'%(x[0],x[1],x[2],x[3],x[4],x[5]))
fp.close()
fpw.close()
