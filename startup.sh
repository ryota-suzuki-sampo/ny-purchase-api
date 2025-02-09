#!/bin/bash
echo "🚀 Starting FastAPI Application..."
cd /home/site/wwwroot
python3 -m uvicorn main:app --host 0.0.0.0 --port 8000 --workers 1