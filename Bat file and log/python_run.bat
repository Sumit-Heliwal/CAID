@echo off

:start
cls
set mypath=%cd%E:\CAID\CAID\
@echo %mypath%

cd /d "E:\CAID\CAID\" 
call venv\Scripts\activate.bat

@echo Starting server and Opening browser...
timeout /t 5 /nobreak

start "" http://127.0.0.1:8000/
python manage.py runserver 8000
pause
exit

