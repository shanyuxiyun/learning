@echo off
set WORK_DIR=%CD%
set HOSTS_PATH=C:\WINDOWS\system32\drivers\etc
set CURL_CMD=%WORK_DIR%\download\curl.exe

%CURL_CMD% -k -# -O https://raw.githubusercontent.com/racaljk/hosts/master/hosts
copy %HOSTS_PATH%\hosts %HOSTS_PATH%\hosts.bak
DEL %HOSTS_PATH%\hosts
copy hosts %HOSTS_PATH%
DEL hosts

CD %WORK_DIR%