import numpy as np
from math import *
import matplotlib.pyplot as mpl
import matplotlib.pyplot as plt
from pylab import *



from pylab import *
input_data= open("entropy_proline_number_spacing_data.dat", "r")
file_content =input_data.readlines()
input_data.close()
ind1=[]
ind2=[]
entropy=[]
entropy1=[]
for x in file_content:
    ind1.append(x.split(' ')[0])
    ind2.append(x.split(' ')[1])
    entropy.append(x.split(' ')[2])
    entropy1.append(x.split(' ')[2])
print(len(ind2))
av_entropy= np.zeros((4,4))
nparray_entropy = np.array(entropy)
nparray_entropy1 = np.array(entropy1)
for i in range(0,4):
    for j in range(0,4):
        sum_entropy=0
        count=0
        for x in range(0, len(entropy)):
            #print(x)
            #print(int(ind1[x]))
            if int(int(ind1[x])==i and int(ind2[x])==j): 
                #print(x)
                sum_entropy=sum_entropy+(float(nparray_entropy[x])-float(nparray_entropy[0]))+(float(nparray_entropy1[x])-float(nparray_entropy1[0]))
                count=count+int(1)
        if int(count) != 0:      
           sum_entropy=sum_entropy/count
           sum_entropy=sum_entropy/2
       
        av_entropy[i,j]=sum_entropy
print((av_entropy))
av_entropy_transpose = av_entropy.T

rc('axes', linewidth=3)
plt.xlabel('Np', fontsize=16, fontweight='bold')


plt.ylabel('Total Spacing', fontsize=16, fontweight='bold')
plt.yticks(fontsize=16)
plt.xticks(fontsize=16)
#plt.xlim(-0.5,3.5)
#plt.ylim(2.5, -0.5)

#plt.autoscale()
plt.imshow(av_entropy_transpose, cmap='gray', interpolation='nearest')
plt.xticks(np.arange(-0.5, 3.5, 0.5))
plt.yticks(np.arange(-0.5, 2.5, 0.5))
plt.xlim(-0.5,3.5)
plt.ylim(2.5, -0.5)
plt.clim(-80,0.0)
plt.colorbar()
plt.savefig("plot_2d_proline_entropy.png",bbox_inches = "tight" )
plt.show()

