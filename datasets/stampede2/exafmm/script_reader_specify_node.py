import numpy as np

# Goal here is to cut the dataset into specific architectural parameters

nnodes=1

# Must randomize when selecting a test set from this dataset because the data had been entered one (ppn,tpr) at a time
fp = open('kt1.csv','r')
fpw = open('kt1_nnodes%d.csv'%(nnodes),'w')
lines = fp.readlines()
#fpw.write(lines[0])

# Apparently cannot shuffle if the list is accessed as [1:] upon argument, so I temporarily removed the header
np.random.shuffle(lines)

for line in lines:
    x = line.split(',')
    if (int(x[1])==nnodes):
        fpw.write('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s'%(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9],x[10],x[11],x[12],x[13],x[14],x[15],x[16],x[17]))
fp.close()
fpw.close()
