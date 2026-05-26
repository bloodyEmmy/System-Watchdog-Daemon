#!/bin/bash

if [[ "$#" -ne 1 ]]; then
    echo "Ошибка: должен быть 1 аргумент - файл access.log" >&2
    exit 1
elif ! [[ -f "$1"  ]]; then
    echo "Файла access.log не существует" >&2
    exit 1
else
    number_uniq_ip=$(awk '{print $1}' "$1" | sort | uniq | wc -l)
    echo "Количество уникальных IP - ${number_uniq_ip}" >&1

    top_spamers=$(awk '{print $1}' "$1" | sort | uniq -c | sort -nr | head -n 3)
    echo "Топ спамеров:" >&1
    echo "${top_spamers}" >&1
fi