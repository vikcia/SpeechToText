@echo off
cd /d %~dp0
start cmd /k ".venv\Scripts\activate && pip install -r requirements.txt && cd src && python main.py"