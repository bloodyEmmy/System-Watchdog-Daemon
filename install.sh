#!/bin/bash

CURRENT_ADDRESS=$(pwd)
sed "s|{{WORKDIR}}|$CURRENT_ADDRESS|g" watchdog.service.template > watchdog.service
sudo cp watchdog.service /etc/systemd/system/
sudo systemctl daemon-reload

echo "Установка завершена! Теперь можно использовать control.sh"