@echo off
title Django Portable Environment v2.5
setlocal enabledelayedexpansion

REM === ���o�Ұʾ��Ҧb�Ϻ� (���ެO E:\ F:\ G:\) ===
set "BASE=%~d0"

REM === �]�w Python �P Django �M�׸��| ===
set "PYTHON=%BASE%\Python\python.exe"
set "PROJECT_DIR=%BASE%\mydjango"
set "VENV_DIR=%PROJECT_DIR%\venv"

echo ==================================================
echo [*] �i�⦡ Python + Django �Ұʾ� v2.5
echo �Ұʾ��Ϻ� : %BASE%
echo Python ��m : %PYTHON%
echo �M�׸��|   : %PROJECT_DIR%
echo ==================================================

REM === �ˬd Python �O�_�s�b ===
if not exist "%PYTHON%" (
    echo [!] �䤣�� Python: %PYTHON%
    echo �нT�{ Python ��Ƨ��P�Ұʾ��b�P�@�h�C
    pause
    exit /b
)

REM === �ˬd�������ҬO�_�s�b�A�Y�S���h�إ� ===
if not exist "%VENV_DIR%" (
    echo [*] �إߵ�������...
    "%PYTHON%" -m venv "%VENV_DIR%"
    echo [?] �������ҫإߧ����I
)

REM === �Ұʵ������� ===
call "%VENV_DIR%\Scripts\activate.bat"

:MENU
cls
echo ==================================================
echo [1] �Ұ� Django ���A��
echo [2] �u�i�J�������� (�R�O�C�Ҧ�)
echo [3] �w�� requirements.txt �M��
echo [4] ���� makemigrations + migrate
echo [5] �۰ʦw�� Django
echo [6] ���}
echo ==================================================
set /p choice=�п�J�ﶵ (1-6): 

if "%choice%"=="1" goto STARTSERVER
if "%choice%"=="2" goto ENTERVENV
if "%choice%"=="3" goto INSTALLREQ
if "%choice%"=="4" goto MIGRATE
if "%choice%"=="5" goto INSTALLDJANGO
if "%choice%"=="6" goto END
echo [!] �L�Ī��ﶵ�A�Э��s��J�C
pause
goto MENU

:STARTSERVER
cd /d "%PROJECT_DIR%"
echo [*] �Ұ� Django ���A�� (http://127.0.0.1:8000) ...
start http://127.0.0.1:8000
python manage.py runserver
pause
goto MENU

:ENTERVENV
echo [*] �A�{�b�w�i�J�������ҡA�i�H��ʿ�J���O�C
echo [����] ��J exit �i��^�Ұʾ����C
cmd
goto MENU

:INSTALLREQ
cd /d "%PROJECT_DIR%"
if exist requirements.txt (
    echo [*] ������ requirements.txt�A�}�l�w�ˮM��...
    pip install -r requirements.txt
    echo [?] requirements �w�˧����I
) else (
    echo [!] �S��� requirements.txt
)
pause
goto MENU

:MIGRATE
cd /d "%PROJECT_DIR%"
echo [*] ���� makemigrations...
python manage.py makemigrations
echo [*] ���� migrate...
python manage.py migrate
echo [?] ��Ʈw�E�������I
pause
goto MENU

:INSTALLDJANGO
echo [*] �}�l�w�� Django...
pip install django
if %errorlevel% neq 0 (
    echo [!] Django �w�˥��ѡA���ˬd������ pip �]�w�C
) else (
    echo [?] Django �w�˦��\�I
    python -m django --version
)
pause
goto MENU

:END
echo [*] ���} Django �Ұʾ�
endlocal
exit
