@echo on
set CURRENT=%CD%
set HOME=E:\Liz\repos\git\hosts
set HOSTS_PATH=C:\WINDOWS\system32\drivers\etc
cd /d %HOME%
git pull
copy %HOSTS_PATH%\hosts %HOSTS_PATH%\hosts.bak
DEL %HOSTS_PATH%\hosts
copy hosts %HOSTS_PATH%

CD %CURRENT%