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

mem_percent = mem_available / mem_total
if mem_percent <= 0.15:
	print("Недостаточно ОЗУ")
else:
	print("Озу в норме")

with open("/proc/loadavg", "r") as file:
	list_values = file.read().split()
	la_1, la_5, la_15 = float(list_values[0]), float(list_values[1]), float(list_values[2])
print(la_1, la_5, la_15)