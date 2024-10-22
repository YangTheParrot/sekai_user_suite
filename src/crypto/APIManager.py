import os
import base64
from dotenv import load_dotenv

load_dotenv()

# load keys and ivs
SEKAI_EN_APIMANAGER_KEY = bytearray(base64.b64decode(os.getenv('SEKAI_EN_APIMANAGER_KEY')))
SEKAI_EN_APIMANAGER_IV = bytearray(base64.b64decode(os.getenv('SEKAI_EN_APIMANAGER_IV')))

SEKAI_JP_APIMANAGER_KEY = bytearray(base64.b64decode(os.getenv('SEKAI_JP_APIMANAGER_KEY')))
SEKAI_JP_APIMANAGER_IV = bytearray(base64.b64decode(os.getenv('SEKAI_JP_APIMANAGER_IV')))

from Crypto.Cipher import AES 
from Crypto.Util.Padding import unpad
import msgpack

# decrypt response for en server
def decrypt_en(ciphertext: bytes) -> bytes:
    cipher = AES.new(SEKAI_EN_APIMANAGER_KEY, AES.MODE_CBC, SEKAI_EN_APIMANAGER_IV)
    plaintext: bytes = unpad(cipher.decrypt(ciphertext), 16)
    return plaintext

# decrypt response for jp server
def decrypt_jp(ciphertext: bytes) -> bytes:
    cipher = AES.new(SEKAI_JP_APIMANAGER_KEY, AES.MODE_CBC, SEKAI_JP_APIMANAGER_IV)
    plaintext: bytes = unpad(cipher.decrypt(ciphertext), 16)
    return plaintext

# unpack the decrypted response
def unmsgpack(ciphertext: bytes, server: str) -> bytes:
    if server == "EN":
        return msgpack.unpackb(decrypt_en(ciphertext), raw=False)
    elif server == "JP":
        return msgpack.unpackb(decrypt_jp(ciphertext), raw=False)
    else:
        raise ValueError("Wtf server?")
