import hashlib
from .settings import SALT

def generate_token(telegram_id):
    token_data = f"{SALT}:{telegram_id}"
    token = hashlib.sha256(token_data.encode()).hexdigest()
    return token
