import time
import read_proc_log_hardware as sensors

def main():
    while True:
        cpu_total, cpu_per_core = sensors.check_cpu_usage()
        free_disk_percent = sensors.check_disk()
        free_mem_percent = sensors.read_free_mem()
        la_1, la_5, la_15 = sensors.read_load_average()
        ips = sensors.read_log_for_ip()

        time.sleep(10)