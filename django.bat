@echo off
title Django Portable Environment v2.5
setlocal enabledelayedexpansion

REM === 取得啟動器所在磁碟 (不管是 E:\ F:\ G:\) ===
set "BASE=%~d0"

REM === 設定 Python 與 Django 專案路徑 ===
set "PYTHON=%BASE%\Python\python.exe"
set "PROJECT_DIR=%BASE%\mydjango"
set "VENV_DIR=%PROJECT_DIR%\venv"

echo ==================================================
echo [*] 可攜式 Python + Django 啟動器 v2.5
echo 啟動器磁碟 : %BASE%
echo Python 位置 : %PYTHON%
echo 專案路徑   : %PROJECT_DIR%
echo ==================================================

REM === 檢查 Python 是否存在 ===
if not exist "%PYTHON%" (
    echo [!] 找不到 Python: %PYTHON%
    echo 請確認 Python 資料夾與啟動器在同一層。
    pause
    exit /b
)

REM === 檢查虛擬環境是否存在，若沒有則建立 ===
if not exist "%VENV_DIR%" (
    echo [*] 建立虛擬環境...
    "%PYTHON%" -m venv "%VENV_DIR%"
    echo [?] 虛擬環境建立完成！
)

REM === 啟動虛擬環境 ===
call "%VENV_DIR%\Scripts\activate.bat"

:MENU
cls
echo ==================================================
echo [1] 啟動 Django 伺服器
echo [2] 只進入虛擬環境 (命令列模式)
echo [3] 安裝 requirements.txt 套件
echo [4] 執行 makemigrations + migrate
echo [5] 自動安裝 Django
echo [6] 離開
echo ==================================================
set /p choice=請輸入選項 (1-6): 

if "%choice%"=="1" goto STARTSERVER
if "%choice%"=="2" goto ENTERVENV
if "%choice%"=="3" goto INSTALLREQ
if "%choice%"=="4" goto MIGRATE
if "%choice%"=="5" goto INSTALLDJANGO
if "%choice%"=="6" goto END
echo [!] 無效的選項，請重新輸入。
pause
goto MENU

:STARTSERVER
cd /d "%PROJECT_DIR%"
echo [*] 啟動 Django 伺服器 (http://127.0.0.1:8000) ...
start http://127.0.0.1:8000
python manage.py runserver
pause
goto MENU

:ENTERVENV
echo [*] 你現在已進入虛擬環境，可以手動輸入指令。
echo [提示] 輸入 exit 可返回啟動器選單。
cmd
goto MENU

:INSTALLREQ
cd /d "%PROJECT_DIR%"
if exist requirements.txt (
    echo [*] 偵測到 requirements.txt，開始安裝套件...
    pip install -r requirements.txt
    echo [?] requirements 安裝完成！
) else (
    echo [!] 沒找到 requirements.txt
)
pause
goto MENU

:MIGRATE
cd /d "%PROJECT_DIR%"
echo [*] 執行 makemigrations...
python manage.py makemigrations
echo [*] 執行 migrate...
python manage.py migrate
echo [?] 資料庫遷移完成！
pause
goto MENU

:INSTALLDJANGO
echo [*] 開始安裝 Django...
pip install django
if %errorlevel% neq 0 (
    echo [!] Django 安裝失敗，請檢查網路或 pip 設定。
) else (
    echo [?] Django 安裝成功！
    python -m django --version
)
pause
goto MENU

:END
echo [*] 離開 Django 啟動器
endlocal
exit
