import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="c:/Users/nhleb/Desktop/PLP_Software_Development/3_Introduction_to_databases/Week8/library_project/library-management-api/api/.env")

conn = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

# Debug prints
print("DB_HOST:", os.getenv("DB_HOST"))
print("DB_USER:", os.getenv("DB_USER"))
print("DB_PASSWORD:", os.getenv("DB_PASSWORD"))
print("DB_NAME:", os.getenv("DB_NAME"))