@echo off
set HOME=%CD%
set HOSTS_PATH=C:\WINDOWS\system32\drivers\etc
set CURL_CMD=%HOME%\download\curl.exe

%CURL_CMD% -k -# -O https://raw.githubusercontent.com/racaljk/hosts/master/hosts
copy %HOSTS_PATH%\hosts %HOSTS_PATH%\hosts.bak
DEL %HOSTS_PATH%\hosts
copy hosts %HOSTS_PATH%

CD %HOME%