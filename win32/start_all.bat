@echo off

taskkill /f /im astrond.exe
taskkill /f /im ppython.exe
taskkill /f /fi "windowtitle eq Toontown Archipelago - UberDOG Server"
taskkill /f /fi "windowtitle eq Toontown Archipelago - Astron Server"
taskkill /f /fi "windowtitle eq Toontown Archipelago - AI (District) Server"
taskkill /f /fi "windowtitle eq Toontown Archipelago - Game Client"

start start_astron_server.bat

ping 192.0.2.2 -n 1 -w 300 > nul
start start_uberdog_server.bat

ping 192.0.2.2 -n 1 -w 300 > nul
start start_ai_server.bat

ping 192.0.2.2 -n 1 -w 1500 > nul
start start_game.bat