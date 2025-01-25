import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent.parent
env_path = BASE_DIR.parent / ".env"
load_dotenv(dotenv_path=env_path)

API_TOKEN = os.environ.get("API_KEY")
SALT = os.environ.get("TOK_SALT")
API_URL = os.environ.get("API_URL")

