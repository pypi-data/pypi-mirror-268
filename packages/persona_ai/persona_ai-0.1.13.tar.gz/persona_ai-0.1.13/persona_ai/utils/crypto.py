from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Util.Padding import pad, unpad
import base64


def encrypt_aes256(key: str, plaintext: str) -> str:
    key = SHA256.new(key.encode()).digest()
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
    return base64.b64encode(cipher.iv + ciphertext).decode()


def decrypt_aes256(key: str, data: str) -> str:
    key = SHA256.new(key.encode()).digest()
    byte_data = base64.b64decode(data)
    iv = byte_data[:16]
    ciphertext = byte_data[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return plaintext.decode()
