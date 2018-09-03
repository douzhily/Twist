#!/usr/bin/python

import os
import subprocess
import time

devices = os.popen('adb devices').readlines()

pkg_name = raw_input('Please enter package name : ').split()[0]

def get_mem_info(pkg_name, native_heap_data, dalvic_heap_data):

	cmd = 'adb shell dumpsys meminfo ' + pkg_name
	meminfo = subprocess.Popen(cmd, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE).stdout.readlines()
	for mem_i in meminfo:
		#print mem_i
		native_heap_id = str(mem_i).find('Native Heap')
		dalvic_heap_id = str(mem_i).find('Dalvik Heap')
		if native_heap_id > 0:
			print mem_i
			native_info = mem_i.split()[2]
			native_heap_data.append(int(native_info))
		elif dalvic_heap_id > 0:
			print mem_i
			dalvic_info = mem_i.split()[2]
			dalvic_heap_data.append(int(dalvic_info))
			break

def mem_info_format():
	native_heap_data = []
	dalvic_heap_data = []
	times = int(raw_input('enter how many seconds you want to run : '))
	for i in range(times):
		get_mem_info(pkg_name, native_heap_data, dalvic_heap_data)
		time.sleep(1)
	print native_heap_data
	print dalvic_heap_data
	return times, native_heap_data, dalvic_heap_data
