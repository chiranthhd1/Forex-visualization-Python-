

import matplotlib.pyplot as plt
import numpy as np
 
file2 = open ("gbpusd.csv")
file1 = open ("ilu.txt", 'w')

row=0
for line in file2:
	test_Samples = line.strip().split(",")
	if(row >0):
		file1.write(test_Samples[3])
		file1.write("\n")
	row +=1

data=np.loadtxt('ilu.txt')
sorted_data = np.sort(data)
cumulative = np.cumsum(sorted_data)
plt.plot(cumulative)
plt.show()



"""
if(row >=0):
		data.append(test_Samples[3])

data = float(data)


num_bins = 100 
counts, bin_edges = np.histogram(data, bins=num_bins, normed=True)

cdf = np.cumsum(counts)
plt.plot(bin_edges[1:], cdf)
plt.xlabel("delay in ms")
plt.ylabel("Probablity")
plt.title("Cumulative Distributive Function(CDF)")

plt.plot(data)
plt.show()
"""		

