@ECHO OFF
SET SETX_CMD=%CD%\setx.exe

SET M2_HOME=D:\ProgramFiles\apache-maven-3.3.9



%SETX_CMD% M2_HOME %M2_HOME%
%SETX_CMD% PATH "%PATH%;%M2_HOME%\bin"