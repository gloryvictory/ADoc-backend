from dotenv import load_dotenv
import os
from time import strftime  # Load just the strftime Module from Time

load_dotenv()

API_VERSION = "/api/v1"

SERVER_HOST = os.getenv("SERVER_HOST", "0.0.0.0")
SERVER_PORT = os.getenv("SERVER_PORT", 8002)

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", 5432)
DB_NAME = os.getenv("DB_NAME", "adoc")
DB_SCHEMA = os.getenv("DB_SCHEMA", "adoc")
DB_USER = os.getenv("DB_USER", "adoc")
DB_PASS = os.getenv("DB_PASS", "adocpwd")
DB_DSN = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
# print(DATABASE_URL)

DATETIME_CURRENT = str(strftime("%Y-%m-%d-%H-%M-%S"))

FOLDER_OUT = 'log'
FILE_LOG_NAME = 'adoc'
FILE_LOG = DATETIME_CURRENT + '_' + FILE_LOG_NAME + '.log'
FILE_LOG_FORMAT = '%(asctime)s %(levelname)s %(message)s'

# FOLDER_BASE = os.getenv("FOLDER_BASE", "C:\\Glory\\Projects\\Python\\zsniigg\\adoc\\src")
