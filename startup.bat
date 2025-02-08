@echo off
SET PATH=%CD%\venv\Scripts;%PATH%
uvicorn main:app --host 0.0.0.0 --port 8000
