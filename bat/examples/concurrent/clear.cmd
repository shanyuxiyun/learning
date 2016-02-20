@echo off
echo please wait to the folders to disappear... 
for /d %%i in (*) do (
    start /b rmdir /s /q %%i 
)
