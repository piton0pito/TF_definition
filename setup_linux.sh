#!/bin/bash

# Получаем версию Python
PYTHON_VERSION=$(python3 --version | cut -d " " -f 2)

# Извлекаем минорную версии
MINOR_VERSION=$(echo $PYTHON_VERSION | cut -d "." -f 2)

# Формируем URL для скачивания TensorFlow
TENSORFLOW_WHEEL_URL="https://files.pythonhosted.org/packages/ba/1c/370b5546cf7afc29649b2fb74c171ef2493a36f62cf901c1425ead4a56af/tensorflow-2.19.0-cp3${MINOR_VERSION}-cp3${MINOR_VERSION}-manylinux_2_17_x86_64.manylinux2014_x86_64.whl"

# Скачиваем TensorFlow
wget "$TENSORFLOW_WHEEL_URL"

# Устанавливаем TensorFlow
pip install "tensorflow-2.19.0-cp3${MINOR_VERSION}-cp3${MINOR_VERSION}-manylinux_2_17_x86_64.whl"

# Устанавливаем зависимости из requirements.txt
pip install -r requirements.txt

echo "DONE"