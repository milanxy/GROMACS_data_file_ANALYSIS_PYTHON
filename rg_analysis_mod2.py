import numpy as np
import glob
import statistics
import matplotlib as mpl
import matplotlib.pyplot as plt
from pylab import *
time=[]
rg=[]
rgx=[]
rgy=[]
rgz=[]
numprolines=[]
totalspace=[]
seq_rg_mean=[]
seq_rg_std=[]
seq_rg_mean2=[]
seq_rg_std2 =[]
seq_rg_final_mean=[]
with open('seq_rgs/entropy_proline_number_spacing_data_removed_aromatic.dat') as f:
     lines = f.readlines()
     #print(lines[1])
    
     for x in lines:
         numprolines.append(x.split(' ')[0])
         totalspace.append(x.split(' ')[1])
f.close()
for infile in sorted(glob.glob('seq_rgs/*.xvg')):
        print ("Current File Being Processed is: " + infile)
#for line in infile:
        content=open(infile, "r") 
        for i in content:
           if not i.startswith("#"):
              if not i.startswith("@"):
                cols=i.split()
                #print(len(cols))
            #if not i.startswith("#"):
        
                if len(cols) == 5:
                   time.append(float(cols[0]))
                   rg.append(float(cols[1]))
                   rgx.append(float(cols[2]))
                   rgy.append(float(cols[3]))
                   rgz.append(float(cols[4]))
        print(len(rg))
        seq_rg_mean.append(statistics.mean(rg))
        seq_rg_std.append(statistics.stdev(rg))
        time.clear()
        rg.clear()
        rgx.clear()
        rgy.clear()
        rgz.clear()
print(len(seq_rg_mean))


for infile in sorted(glob.glob('seq_rgs_run2/*.xvg')):
        print ("Current File Being Processed is: " + infile)
#for line in infile:
        content=open(infile, "r")
        for i in content:
           if not i.startswith("#"):
              if not i.startswith("@"):
                cols=i.split()
                #print(len(cols))
            #if not i.startswith("#"):

                if len(cols) == 5:
                   time.append(float(cols[0]))
                   rg.append(float(cols[1]))
                   rgx.append(float(cols[2]))
                   rgy.append(float(cols[3]))
                   rgz.append(float(cols[4]))
        print(len(rg))
        seq_rg_mean2.append(statistics.mean(rg))
        seq_rg_std2.append(statistics.stdev(rg))
        time.clear()
        rg.clear()
        rgx.clear()
        rgy.clear()
        rgz.clear()
print(len(seq_rg_mean2))

#seq_rg_final_mean = float(seq_rg_mean) + float(seq_rg_mean2)
seq_rg_final_mean = [seq_rg_mean[i] + seq_rg_mean2[i] for i in range(len(seq_rg_mean))]
myInt =2
seq_rg_final_mean[:] = [x / myInt for x in seq_rg_final_mean]


av_rg= np.zeros((4,4))
nparray_seq_rg_mean = np.array(seq_rg_final_mean)
for i in range(0,4):
    for j in range(0,4):
        sum_rg=0
        count=0
        for x in range(0, len(seq_rg_final_mean)):
            #print(x)
            #print(int(ind1[x]))
            if int(int(numprolines[x])==i and int(totalspace[x])==j): 
                #print(x)
                sum_rg=sum_rg+(float(nparray_seq_rg_mean[x]))
                count=count+int(1)
        if int(count) != 0:      
           sum_rg=sum_rg/count
           #sum_entropy=sum_entropy/2
       
        av_rg[i,j]=sum_rg
print((av_rg))
av_rg_transpose = av_rg.T


rc('axes', linewidth=3)
plt.xlabel('Np', fontsize=16, fontweight='bold')


plt.ylabel('Total Spacing', fontsize=16, fontweight='bold')
plt.yticks(fontsize=16)
plt.xticks(fontsize=16)
#plt.xlim(-0.5,3.5)
#plt.ylim(2.5, -0.5)

#plt.autoscale()
plt.imshow(av_rg_transpose, cmap='gray_r', interpolation='nearest')
plt.xticks(np.arange(-0.5, 3.5, 0.5))
plt.yticks(np.arange(-0.5, 2.5, 0.5))
plt.xlim(-0.5,3.5)
plt.ylim(2.5, -0.5)
plt.clim(0.6,0.8)
plt.colorbar()
plt.savefig("plot_2d_proline_rg.png",bbox_inches = "tight" )
plt.show()

