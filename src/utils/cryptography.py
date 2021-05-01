from cryptography.fernet import Fernet

from src.utils.settings import get_cryptography_key


def _get_instance_cryptography():
    f = Fernet(get_cryptography_key())
    return f


def encrypt(text: str):
    f = _get_instance_cryptography()
    enc_text = f.encrypt(text.encode()).decode()
    return str(enc_text)


def decrypt(text: str):
    f = _get_instance_cryptography()
    dec_text = f.decrypt(text.encode()).decode()
    return str(dec_text)
