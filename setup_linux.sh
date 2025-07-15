#!/bin/bash

# Получаем версию Python
PYTHON_VERSION=$(python3 --version | cut -d " " -f 2)

# Извлекаем минорную версию
MINOR_VERSION=$(echo $PYTHON_VERSION | cut -d "." -f 2)

# Формируем URL для скачивания TensorFlow в зависимости от версии Python
case $MINOR_VERSION in
    9)
        TENSORFLOW_WHEEL_URL="https://files.pythonhosted.org/packages/61/91/0d43cde213a1b65a857d07144cfe170d5083b43467cac5e1806fb758a4cf/tensorflow-2.19.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl"
        ;;
    10)
        TENSORFLOW_WHEEL_URL="https://files.pythonhosted.org/packages/2b/b6/86f99528b3edca3c31cad43e79b15debc9124c7cbc772a8f8e82667fd427/tensorflow-2.19.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl"
        ;;
    11)
        TENSORFLOW_WHEEL_URL="https://files.pythonhosted.org/packages/ba/1c/370b5546cf7afc29649b2fb74c171ef2493a36f62cf901c1425ead4a56af/tensorflow-2.19.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl"
        ;;
    12)
        TENSORFLOW_WHEEL_URL='https://files.pythonhosted.org/packages/01/12/a8ad8322a7cb2818e658a073feb2aa541d0e6a32b8e5ac838d46e0882687/tensorflow-2.19.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl'
        ;;
    *)
        echo "Unsupported Python version: 3.$MINOR_VERSION"
        exit 1
        ;;
esac

echo "Downloading TensorFlow for Python 3.$MINOR_VERSION..."
wget "$TENSORFLOW_WHEEL_URL" || { echo "Download failed"; exit 1; }

WHEEL_FILE=$(basename "$TENSORFLOW_WHEEL_URL")
echo "Installing TensorFlow from $WHEEL_FILE..."
pip install "$WHEEL_FILE" || { echo "Installation failed"; exit 1; }

# Устанавливаем зависимости из requirements.txt если файл существует
if [ -f "requirements.txt" ]; then
    echo "Installing requirements..."
    pip install -r requirements.txt || { echo "Failed to install requirements"; exit 1; }
else
    echo "requirements.txt not found, skipping..."
fi

echo "DONE"