#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Ошибка: Должен быть 1 параметр: start / stop / status"
    echo "start  - запуск программы в фоновом режиме + автозагрузка"
    echo "stop   - остановка программы + вывод из автозагрузки"
    echo "status - текущий статус программы"
    exit 1
fi

COMMAND=$1
SERVICE="watchdog.service"

if [ "$COMMAND" == "start" ]; then
    if systemctl is-active --quiet $SERVICE; then
        echo "Программа уже в рабочем состоянии."
        logger "Watchdog control: Attempted to start, but already running."
    else
        sudo systemctl start $SERVICE
        sudo systemctl enable $SERVICE
        echo "Watchdog запущен и добавлен в автозагрузку."
        logger "Watchdog control: Service started and enabled."
    fi

elif [ "$COMMAND" == "stop" ]; then
    if ! systemctl is-active --quiet $SERVICE; then
        echo "Программа уже выключена."
        logger "Watchdog control: Attempted to stop, but already stopped."
    else
        sudo systemctl stop $SERVICE
        sudo systemctl disable $SERVICE
        echo "Watchdog остановлен и убран из автозагрузки."
        logger "Watchdog control: Service stopped and disabled."
    fi

elif [ "$COMMAND" == "status" ]; then
    sudo systemctl status $SERVICE --no-pager

else
    echo "Ошибка: Неизвестная команда '$COMMAND'."
    exit 1
fi