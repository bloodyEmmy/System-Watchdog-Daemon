#!/bin/bash

if [[ "$#" -ne 1 ]]; then
    echo "Ошибка: должен быть 1 аргумент - файл access.log"
    exit 1
elif ! [[ -f "$1"  ]]; then
    echo "Файла access.log не существует"
    exit 1
else
    number_uniq_ip=$(awk '{print $1}' "$1" | sort | uniq | wc -l)
    echo "Количество уникальных IP - ${number_uniq_ip}"

    top_spamers=$(awk '{print $1}' "$1" | uniq -c | sort -nr | head -n 3)
    echo "Топ спамеров:"
    echo "${top_spamers}"
fi