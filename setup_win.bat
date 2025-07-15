@echo off

REM Создаем виртуальное окружение
echo Creating virtual environment...
python -m venv venv || (
    echo Failed to create virtual environment
    exit /b 1
)

REM Активируем виртуальное окружение
echo Activating virtual environment...
call venv\Scripts\activate || (
    echo Failed to activate virtual environment
    exit /b 1
)

REM Получаем версию Python
for /f "tokens=2 delims= " %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i

REM Извлекаем минорную версию
for /f "tokens=2 delims=." %%i in ("%PYTHON_VERSION%") do set MINOR_VERSION=%%i

REM Формируем URL для скачивания TensorFlow в зависимости от версии Python
if "%MINOR_VERSION%"=="9" (
    set TENSORFLOW_WHEEL_URL=https://files.pythonhosted.org/packages/61/91/0d43cde213a1b65a857d07144cfe170d5083b43467cac5e1806fb758a4cf/tensorflow-2.19.0-cp39-cp39-win_amd64.whl
) else if "%MINOR_VERSION%"=="10" (
    set TENSORFLOW_WHEEL_URL=https://files.pythonhosted.org/packages/2b/b6/86f99528b3edca3c31cad43e79b15debc9124c7cbc772a8f8e82667fd427/tensorflow-2.19.0-cp310-cp310-win_amd64.whl
) else if "%MINOR_VERSION%"=="11" (
    set TENSORFLOW_WHEEL_URL=https://files.pythonhosted.org/packages/ba/1c/370b5546cf7afc29649b2fb74c171ef2493a36f62cf901c1425ead4a56af/tensorflow-2.19.0-cp311-cp311-win_amd64.whl
) else if "%MINOR_VERSION%"=="12" (
    set TENSORFLOW_WHEEL_URL=https://files.pythonhosted.org/packages/01/12/a8ad8322a7cb2818e658a073feb2aa541d0e6a32b8e5ac838d46e0882687/tensorflow-2.19.0-cp312-cp312-win_amd64.whl
) else (
    echo Unsupported Python version: 3.%MINOR_VERSION%
    exit /b 1
)

REM Получаем имя файла из URL
for %%i in ("%TENSORFLOW_WHEEL_URL%") do set WHEEL_FILE=%%~nxi

REM Проверяем, существует ли уже файл
if exist "%WHEEL_FILE%" (
    echo File %WHEEL_FILE% already exists, skipping download.
) else (
    echo Downloading TensorFlow for Python 3.%MINOR_VERSION%...
    curl -O %TENSORFLOW_WHEEL_URL% || (
        echo Download failed
        exit /b 1
    )
)

echo Installing TensorFlow from %WHEEL_FILE%...
pip install %WHEEL_FILE% || (
    echo Installation failed
    exit /b 1
)

REM Устанавливаем зависимости из requirements.txt если файл существует
if exist "requirements.txt" (
    echo Installing requirements...
    pip install -r requirements.txt || (
        echo Failed to install requirements
        exit /b 1
    )
) else (
    echo requirements.txt not found, skipping...
)

echo DONE
echo To activate the virtual environment later, run: venv\Scripts\activate