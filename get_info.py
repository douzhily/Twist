#!/usr/bin/python

import os
import subprocess
import time

devices = os.popen('adb devices').readlines()

package_name = raw_input('Please enter package name : ').split()[0]
grep_info = raw_input('Please enter grep info :').split()[0]

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
	cpu_data = []
	times = int(raw_input('enter how many seconds you want to run : '))
	for i in range(times):
		get_mem_info(package_name, native_heap_data, dalvic_heap_data)
		get_cpu_info(grep_info, cpu_data)
		time.sleep(1)
	print native_heap_data
	print dalvic_heap_data
	print cpu_data
	return times, native_heap_data, dalvic_heap_data, cpu_data

def get_cpu_info(grep_name, cpu_data):
	cmd = 'adb shell top -n 1 | grep ' + grep_name
	print cmd
	cpuinfo = subprocess.Popen(cmd, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE).stdout.readlines()
	print cpuinfo
	cpu_info = cpuinfo[0].split()[8]
	cpu_data.append(float(cpu_info))











