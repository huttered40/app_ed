import sys

# This version of extrapolation requires all but one element to be below a specified integer.

cut = [int(sys.argv[1]),int(sys.argv[2])]
fp = open('/work2/05608/tg849075/app_ed/datasets/stampede2/gemm/1-thread.csv','r')
fpw = open('/work2/05608/tg849075/app_ed/datasets/stampede2/gemm/1-thread-cutv2-%d-%d.csv'%(cut[0],cut[1]),'w')
lines = fp.readlines()
fpw.write(lines[0])
for line in lines[1:]:
    x = line.split(',')
    count=0
    if (int(x[1]) > cut[1]):
        count += 1
    if (int(x[2]) > cut[1]):
        count += 1
    if (int(x[3]) > cut[1]):
        count += 1
    if (count <= 1):
        fpw.write('%s,%s,%s,%s,%s,%s'%(x[0],x[1],x[2],x[3],x[4],x[5]))
fp.close()
fpw.close()
