@echo off

for /d %%i in (*suite) do (
    start %%i\LongTaskTemplate %%i
)