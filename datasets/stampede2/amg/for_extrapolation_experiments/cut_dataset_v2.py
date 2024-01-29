import sys

# This version of extrapolation requires all but one element to be below a specified integer.

cut_nx = [int(sys.argv[1]),int(sys.argv[2])]
cut_ny = [int(sys.argv[1]),int(sys.argv[2])]
cut_nz = [int(sys.argv[1]),int(sys.argv[2])]
#fp = open('/work2/05608/tg849075/app_ed/datasets/stampede2/amg/kt0_nnodes1.csv','r')
#fpw = open('/work2/05608/tg849075/app_ed/datasets/stampede2/amg/kt0_nnodes1_cut-%d-%d_%d-%d_%d-%d.csv'%(cut_nx[0],cut_nx[1],cut_ny[0],cut_ny[1],cut_nz[0],cut_nz[1]),'w')
fp = open('/work2/05608/tg849075/app_ed/datasets/stampede2/amg/kt0_ppn64_tpr1_nnodes1.csv','r')
fpw = open('/work2/05608/tg849075/app_ed/datasets/stampede2/amg/kt0_ppn64_tpr1_nnodes1_cut-%d-%d_%d-%d_%d-%d.csv'%(cut_nx[0],cut_nx[1],cut_ny[0],cut_ny[1],cut_nz[0],cut_nz[1]),'w')
lines = fp.readlines()
fpw.write(lines[0])
for line in lines[1:]:
    x = line.split(',')
    if ((int(x[1]) >= cut_nx[0]) and\
        (int(x[1]) <= cut_nx[1]) and\
        (int(x[2]) >= cut_ny[0]) and\
        (int(x[2]) <= cut_ny[1]) and\
        (int(x[3]) >= cut_nz[0]) and\
        (int(x[3]) <= cut_nz[1])):
        fpw.write('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s'%(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9],x[10],x[11],x[12],x[13],x[14]))
fp.close()
fpw.close()
