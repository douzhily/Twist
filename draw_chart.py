import matplotlib.pyplot as plt
import numpy as np
import get_meminfo
#import random
data = get_meminfo.mem_info_format()
times = data[0]
native_heap = data[1]
dalvic_heap = data[2]
x_axis = np.linspace(0, times, times)
#y_axis = native_heap
plt.figure()
#print x_axis
#print y_axis
plt.plot(x_axis, native_heap, 'r-o', label = 'Native Heap')
plt.plot(x_axis, dalvic_heap, 'g-o', label = 'Dalvic Heap')
plt.legend()
plt.xlabel('time/s')
plt.ylabel('PSS')
plt.title('Memory Infomation')
plt.show()