@echo off
SET HOME=%CD%
SET CURL_CMD=%HOME%\curl.exe
SET DOWNLOADS=downloads
SET URLS=%HOME%\URLs.txt

mkdir %DOWNLOADS%
cd %DOWNLOADS%


FOR /F %%i in (%URLs%) DO (
	ECHO download : %%i
	START /B %CURL_CMD% -O -k -# %%i
)


CD %HOME%