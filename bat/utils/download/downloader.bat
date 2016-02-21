@echo off
SETlocal enabledelayedexpansion 
SET HOME=%CD%
SET CURL_CMD=%HOME%\curl.exe
SET DOWNLOADS=downloads
SET URLS=%HOME%\URLs.txt

mkdir %DOWNLOADS%
cd %DOWNLOADS%

SET TEMP=
SET comment=
FOR /F %%i in (%URLs%) DO (
	SET TEMP=%%i
	CALL :check_comment !TEMP!
	IF "X!comment!" == "X" (
		ECHO download : !TEMP!
	    START /B %CURL_CMD% -O -k -# !TEMP!
	)
	SET "comment="
)

CD %HOME%

:check_comment
SET "line=%1"
FOR /f "delims=" %%j in (' ECHO %line% ^| FINDSTR /R /C:"^#.*$" ') do (
		SET "comment=%%j"
	    SET "comment=!comment!"
)