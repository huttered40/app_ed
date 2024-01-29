import sys

# This version of extrapolation requires all elements to be below a specified integer.

cut_num_bodies = [int(sys.argv[1]),int(sys.argv[2])]
fp = open('/work2/05608/tg849075/app_ed/datasets/stampede2/exafmm/exafmm_kt0_node1_ppn64_tpr1_nnodes1.csv','r')
fpw = open('/work2/05608/tg849075/app_ed/datasets/stampede2/exafmm/exafmm_kt0_node1_ppn64_tpr1_nnodes1.csv_cut--%d-%d.csv'%(cut_num_bodies[0],cut_num_bodies[1]),'w')
lines = fp.readlines()
fpw.write(lines[0])
for line in lines[1:]:
    x = line.split(',')
    if ((int(x[4]) >= cut_num_bodies[0]) and\
        (int(x[4]) <= cut_num_bodies[1])):
        fpw.write('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s'%(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9],x[10],x[11],x[12],x[13],x[14],x[15],x[16],x[17]))
fp.close()
fpw.close()
