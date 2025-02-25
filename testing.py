import os
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv("DB_HOST")

print(HOST)
