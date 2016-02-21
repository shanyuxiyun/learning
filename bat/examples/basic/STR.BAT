@ECHO OFF

set x=0123456789
REM 从右向左截取8个字符
echo.X=%x:~-8%
REM 从左第3个位置开始截取4个字符
echo X=%x:~2,4%
REM  替换
echo X=%x:456=ABC%
REM 删除
echo X=%x:456=%

for /f  "tokens=1,2,3 delims=-" %%i in ("%date%") do (
	echo %%i 
	echo %%j 
	set day=%%k
	echo.%day%
	echo %day:~0,2%
)

pause
