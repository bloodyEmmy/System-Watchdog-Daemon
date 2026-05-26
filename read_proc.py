mem_total = 0
mem_available = 0

with open("/proc/meminfo", "r") as file:
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