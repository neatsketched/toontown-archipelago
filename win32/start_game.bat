@echo off
title Toontown Archipelago - Game Client
cd..

rem Read the contents of PPYTHON_PATH into %PPYTHON_PATH%:
set /P PPYTHON_PATH=<PPYTHON_PATH

set TTOFF_LOGIN_TOKEN=dev
:launcher
%PPYTHON_PATH% -m toontown.launcher.TTOffQuickStartLauncher
pause
goto :launcher
