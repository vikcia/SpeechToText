@echo off
cd /d %~dp0
start cmd /k ".venv\Scripts\activate && cd src && python main.py"