import sys

# This version of extrapolation requires all elements to be below a specified integer.

cut_m = [int(sys.argv[1]),int(sys.argv[2])]
cut_n = [int(sys.argv[3]),int(sys.argv[4])]
cut_k = [int(sys.argv[5]),int(sys.argv[6])]
fp = open('/work2/05608/tg849075/app_ed/datasets/stampede2/gemm/1-thread.csv','r')
fpw = open('/work2/05608/tg849075/app_ed/datasets/stampede2/gemm/1-thread-cut--%d-%d--%d-%d--%d-%d.csv'%(cut_m[0],cut_m[1],cut_n[0],cut_n[1],cut_k[0],cut_k[1]),'w')
lines = fp.readlines()
fpw.write(lines[0])
for line in lines[1:]:
    x = line.split(',')
    if ((int(x[1]) >= cut_m[0]) and\
        (int(x[1]) <= cut_m[1]) and\
        (int(x[2]) >= cut_n[0]) and\
        (int(x[2]) <= cut_n[1]) and\
        (int(x[3]) >= cut_k[0]) and\
        (int(x[3]) <= cut_k[1])):
        fpw.write('%s,%s,%s,%s,%s,%s'%(x[0],x[1],x[2],x[3],x[4],x[5]))
fp.close()
fpw.close()
