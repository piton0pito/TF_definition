@echo off

REM Получаем версию Python
for /f "tokens=2 delims= " %%i in ('python --version') do set PYTHON_VERSION=%%i

REM Извлекаем минорную версию
for /f "tokens=2 delims=." %%i in ("%PYTHON_VERSION%") do set MINOR_VERSION=%%i

REM Формируем URL для скачивания TensorFlow
set TENSORFLOW_WHEEL_URL=https://files.pythonhosted.org/packages/ba/1c/370b5546cf7afc29649b2fb74c171ef2493a36f62cf901c1425ead4a56af/tensorflow-2.19.0-cp3%MINOR_VERSION%-cp3%MINOR_VERSION%-win_amd64.whl

REM Скачиваем TensorFlow
curl -O %TENSORFLOW_WHEEL_URL%

REM Устанавливаем TensorFlow
pip install tensorflow-2.19.0-cp3%MINOR_VERSION%-cp3%MINOR_VERSION%-win_amd64.whl

REM Устанавливаем зависимости из requirements.txt
pip install -r requirements.txt

echo DONE