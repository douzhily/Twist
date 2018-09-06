import matplotlib.pyplot as plt
import numpy as np
import get_info



def draw_heap_data(times, native_heap, dalvic_heap):
	x_axis = np.linspace(0, times, times)	

	plt.figure()
	plt.plot(x_axis, native_heap, 'r-o', label = 'Native Heap')
	plt.plot(x_axis, dalvic_heap, 'g-o', label = 'Dalvic Heap')
	plt.legend()
	plt.xlabel('time/s')
	plt.ylabel('PSS')
	plt.title('Memory Infomation')
	plt.show()

def draw_cpu_data(times, cpu_data):
	x_axis = np.linspace(0, times, times)	

	plt.figure()
	plt.plot(x_axis, cpu_data, 'g-o', label = 'CPU')
	plt.legend()
	plt.xlabel('time/s')
	plt.ylabel('%')
	plt.title('CPU Infomation')
	plt.show()

def draw():
	data = get_info.info_format()
	times = data[0]
	native_heap = data[1]
	dalvic_heap = data[2]
	cpu_data = data[3]
	draw_heap_data(times, native_heap, dalvic_heap)
	draw_cpu_data(times, cpu_data)
