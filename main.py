import time
import syslog
from syslog_write import syslog_write

def main():
    syslog.openlog(ident="sys_watchdog", facility=syslog.LOG_DAEMON)
    syslog.syslog(syslog.LOG_INFO, "Watchdog запущен. Мониторинг начат.")

    while True:
        try:
            syslog_write()
            time.sleep(10)
        except FileNotFoundError as e:
            syslog.syslog(syslog.LOG_ERR, f"ERROR: Потерян системный файл: {e}")
            time.sleep(10)
        except Exception as e:
            syslog.syslog(syslog.LOG_ERR, f"ERROR: Непредвиденная ошибка цикла: {e}")
            time.sleep(10)