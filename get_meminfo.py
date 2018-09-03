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
			native_heap_data.append(int(native_info))
		elif dalvic_heap_id == 2:
			print mem_i
			dalvic_info = mem_i.split()[2]
			dalvic_heap_data.append(int(dalvic_info))

def mem_info_format():
	native_heap_data = []
	dalvic_heap_data = []
	times = int(raw_input())
	for i in range(times):
		get_mem_info(pkg_name, native_heap_data, dalvic_heap_data)
		time.sleep(1)
	print native_heap_data
	print dalvic_heap_data
	return times, native_heap_data, dalvic_heap_data

#x = mem_info_format()
#print x[1]