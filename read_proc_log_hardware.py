import psutil
import shutil

def check_cpu_usage():
	cpu_total = psutil.cpu_percent(interval=1.0)
	cpu_per_core = psutil.cpu_percent(interval=1.0, percpu=True)
	return cpu_total, cpu_per_core

def check_disk():
	total, used, free = psutil.disk_usage("/")
	free_disk_percent = free / total * 100
	return free_disk_percent

def read_free_mem():
	with open("/proc/meminfo", "r") as file:
		mem_total = 0
		mem_available = 0
		for line in file:
			if line.startswith("MemTotal: "):
				mem_total = int(line.split()[1])
			elif line.startswith("MemAvailable: "):
				mem_available = int(line.split()[1])
			if mem_total > 0 and mem_available > 0:
				break
	free_mem_percent = mem_available / mem_total * 100
	return free_mem_percent

def read_load_average():
	with open("/proc/loadavg", "r") as file:
		list_values = file.read().split()
		la_1, la_5, la_15 = float(list_values[0]), float(list_values[1]), float(list_values[2])
	return la_1, la_5, la_15

def read_log(filename):
	ips = dict()
	with open(filename, "r") as file:
		for line in file:
			ips[line.split()[0]] = 1
			if line.split()[0] in ips:
				ips[line.split()[0]] += 1
	return ips