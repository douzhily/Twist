#!/usr/bin/python

import os
import subprocess
import time

devices = os.popen('adb devices').readlines()


def get_pid():
	package_name = raw_input('Please enter package name : ').split()[0]
	print package_name
	cmd = 'adb shell ps | grep ' + package_name
	pidinfo = subprocess.Popen(cmd, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE).stdout.readlines()
	#print pidinfo
	for pid_i in pidinfo:
		pid_name = pid_i.split()[9]
		if pid_name == package_name:
			pid = pid_i.split()[1]
			print ('PID of ' + package_name + ' is ' + str(pid))
			return int(pid)


def get_mem_info(pid, native_heap_data, dalvic_heap_data):

	cmd = 'adb shell dumpsys meminfo ' + str(pid)
	meminfo = subprocess.Popen(cmd, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE).stdout.readlines()
	for mem_i in meminfo:
		#print mem_i
		native_heap_id = str(mem_i).find('Native Heap')
		dalvic_heap_id = str(mem_i).find('Dalvik Heap')
		if native_heap_id > 0:
			print (mem_i)
			native_info = mem_i.split()[2]
			native_heap_data.append(int(native_info))
		elif dalvic_heap_id > 0:
			print (mem_i)
			dalvic_info = mem_i.split()[2]
			dalvic_heap_data.append(int(dalvic_info))
			break


def get_cpu_info(pid, cpu_data):

	cmd = 'adb shell top -n 1 | grep ' + str(pid)
	print (cmd)
	cpuinfo = subprocess.Popen(cmd, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE).stdout.readlines()
	print (cpuinfo)
	cpu_info = cpuinfo[0].split()[8]
	cpu_data.append(float(cpu_info))


def info_format():

	pid = get_pid()
	native_heap_data = []
	dalvic_heap_data = []
	cpu_data = []
	times = int(raw_input('enter how many times you want to run : '))
	for i in range(times):
		get_mem_info(pid, native_heap_data, dalvic_heap_data)
		get_cpu_info(pid, cpu_data)
		time.sleep(1)
	#print native_heap_data
	#print dalvic_heap_data
	#print cpu_data
	return times, native_heap_data, dalvic_heap_data, cpu_data











