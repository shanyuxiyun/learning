@echo off

MODE CON: COLS=90 LINES=10

setlocal

REM 1. set
set /a a=(3+5)*3+10
echo a is %a%

REM System Function
REM GOTO :EOF
GOTO NEXT
set /p b=please input something:
echo your input is %b%
echo. 

endlocal

:NEXT
REM 无条件执行&后面的命令
cls&dir

find "NEXT" alg.bat>NUL && (
	echo "NEXT" Exists alg.bat
)

REM 统计文件行数
SET /A FILE_COUNT=0
FOR /F %%I IN ('TYPE %0  ^| FIND "" /C /V') DO (
	SET FILE_COUNT=%%I
)
ECHO FILE COUNT IS %FILE_COUNT%

REM 扩展
SETLOCAL ENABLEEXTENSIONS
SETLOCAL DISABLEDELAYEDEXPANSION
echo.delayed expansion is DISABLED
echo.1. ^^! :exclamation mark
echo.2. !! :exclamation mark
echo.3. ! :exclamation mark
echo.4. %% :percent
echo.5. ^& :ampersand
echo.6. ^| :vertical line
echo.7. ^^ :caret
echo.

SETLOCAL ENABLEDELAYEDEXPANSION
echo.delayed expansion is ENABLED
echo.1. ^^! :exclamation mark
echo.2. !! :exclamation mark
echo.3. ! :exclamation mark
echo.4. %% :percent
echo.5. ^& :ampersand
echo.6. ^| :vertical line
echo.7. ^^ :caret
echo.

for %%A in (%0) do (
	echo.Size of "%%A" is %%~zA bytes
	echo ~f "%%A" is %%~fA 
	echo ~d "%%A" is %%~dA 
	echo ~p "%%A" is %%~pA
	echo ~dp "%%A" is %%~dpA  

	echo ~n "%%A" is %%~nA
	echo ~x "%%A" is %%~xA
)

REM 分行
echo.1. This all goes ^
in line one

color 1A



ECHO.&PAUSE&GOTO:EOF