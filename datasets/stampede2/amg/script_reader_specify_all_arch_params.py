# Goal here is to cut the dataset into specific architectural parameters

ppn=64
tpr=1
nnodes=1

fp = open('kt0.csv','r')
fpw = open('kt0_ppn%d_tpr%d_nnodes%d.csv'%(ppn,tpr,nnodes),'w')
lines = fp.readlines()
for line in lines[0:]:
    x = line.split(',')
    if (int(x[10])==tpr and int(x[11])==ppn and int(x[12])==nnodes):
        fpw.write('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s'%(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9],x[10],x[11],x[12],x[13],x[14]))
fp.close()
fpw.close()
