from fastapi import FastAPI
import pyodbc
import os

app = FastAPI()

DB_SERVER = os.getenv("DB_SERVER")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

conn_str = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    f"SERVER=tcp:{DB_SERVER},1433;"
    f"DATABASE={DB_NAME};"
    f"UID={DB_USER};"
    f"PWD={DB_PASSWORD};"
    "Encrypt=yes;"
    "TrustServerCertificate=no;"
    "Connection Timeout=30;"
)

# 🔹 DB接続の例外処理を追加
try:
    conn = pyodbc.connect(conn_str)
    conn.close()
except Exception as e:
    print(f"⚠️ Database connection failed: {e}")

@app.get("/")
def read_root():
    return {"message": "FastAPI is running!"}
