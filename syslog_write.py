import syslog
import read_proc_log_hardware as sensors

WARN_CPU_TOTAL = 80.0
CRIT_CPU_TOTAL = 95.0
WARN_CPU_CORE = 90.0
CRIT_CPU_CORE = 98.0
WARN_MEM_PERCENT = 20.0
CRIT_MEM_PERCENT = 5.0
WARN_DISK_PERCENT = 15.0
CRIT_DISK_PERCENT = 5.0
WARN_LA = 8.0   
CRIT_LA = 12.0
WARN_IP_REQS = 50
CRIT_IP_REQS = 200

def syslog_write():
    cpu_total, cpu_per_core = sensors.check_cpu_usage()
    free_disk_percent = sensors.check_disk()
    free_mem_percent = sensors.read_free_mem()
    la_1, la_5, la_15 = sensors.read_load_average()
    ips = sensors.read_log_for_ip("access.log")

    if cpu_total >= CRIT_CPU_TOTAL:
        syslog.syslog(syslog.LOG_CRIT, f"CRITICAL: Общая загрузка CPU критическая: {cpu_total:.1f}%")
    elif cpu_total >= WARN_CPU_TOTAL:
        syslog.syslog(syslog.LOG_WARNING, f"WARNING: Высокая общая загрузка CPU: {cpu_total:.1f}%")

    for i, core_load in enumerate(cpu_per_core):
        if core_load >= CRIT_CPU_CORE:
            syslog.syslog(syslog.LOG_CRIT, f"CRITICAL: Ядро {i} перегружено: {core_load:.1f}%")
        elif core_load >= WARN_CPU_CORE:
            syslog.syslog(syslog.LOG_WARNING, f"WARNING: Высокая нагрузка на ядро {i}: {core_load:.1f}%")

    if free_mem_percent < CRIT_MEM_PERCENT:
        syslog.syslog(syslog.LOG_CRIT, f"CRITICAL: Осталось критически мало памяти: {free_mem_percent:.1f}%")
    elif free_mem_percent < WARN_MEM_PERCENT:
        syslog.syslog(syslog.LOG_WARNING, f"WARNING: Память убывает. Осталось свободно {free_mem_percent:.1f}%")

    for value in [la_1, la_5, la_15]:
        if value > CRIT_LA:
            syslog.syslog(syslog.LOG_CRIT, f"CRITICAL: Система перегружена! LA: {value}")
        elif value > WARN_LA:
            syslog.syslog(syslog.LOG_WARNING, f"WARNING: Нагрузка растет. LA: {value}")
        
    if free_disk_percent < CRIT_DISK_PERCENT:
        syslog.syslog(syslog.LOG_CRIT, f"CRITICAL: Место на диске почти закончилось! Свободно: {free_disk_percent:.1f}%")
    elif free_disk_percent < WARN_DISK_PERCENT:
        syslog.syslog(syslog.LOG_CRIT, f"WARNING: Место на диске скоро закончится! Свободно: {free_disk_percent:.1f}%")

    for ip, count in ips.items():
        if count > CRIT_IP_REQS:
            syslog.syslog(syslog.LOG_CRIT, f"CRITICAL: Аномалия логов! IP {ip} сделал {count} запросов.")
        elif count > WARN_IP_REQS:
            syslog.syslog(syslog.LOG_WARNING, f"WARNING: Подозрительная активность с IP {ip} ({count} запросов).")