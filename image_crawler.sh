#!/bin/bash

# Путь к текстовому файлу
input_file="brand_car.txt"

# Проверка существования файла
if [[ ! -f "$input_file" ]]; then
    echo "Файл $input_file не найден!"
    exit 1
fi

# Чтение файла построчно
while IFS= read -r brand; do
    # Удаление пробелов в начале и конце строки
    brand=$(echo "$brand" | xargs)

    # Выполнение команды
    echo "Запуск: yandex-images-crawler --links \"https://yandex.com/images/search?text=${brand}%20car\" --count 1000 --dir \"data/${brand}\""
    yandex-images-crawler --links "https://yandex.com/images/search?text=${brand}" --count 1100 --dir "data/${brand}"

done < "$input_file"