#!/usr/bin/python

import os
import subprocess
import time

devices = os.popen('adb devices').readlines()
#print devices

pkg_name = 'com.zhihu.android'

def get_mem_info(pkg_name, native_heap_data, dalvic_heap_data):

	cmd = 'adb shell dumpsys meminfo ' + pkg_name
	meminfo = subprocess.Popen(cmd, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE).stdout.readlines()
	for mem_i in meminfo:
		#print mem_i
		native_heap_id = str(mem_i).find('Native Heap')
		dalvic_heap_id = str(mem_i).find('Dalvik Heap')
		if native_heap_id == 2:
			print mem_i
			native_info = mem_i.split()[2]
			native_heap_data.append(native_info)
		elif dalvic_heap_id == 2:
			print mem_i
			dalvic_info = mem_i.split()[2]
			dalvic_heap_data.append(dalvic_info)

native_heap_data = []
dalvic_heap_data = []
for i in range(100):
	get_mem_info(pkg_name, native_heap_data, dalvic_heap_data)

print native_heap_data
print dalvic_heap_data