import hashlib


# --- Утилиты ---
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
