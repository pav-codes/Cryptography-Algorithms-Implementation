#AES - symmetric encryption algorithm

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
key = get_random_bytes(16)

message = "Cyber security internship project 1"
cipher = AES.new(key, AES.MODE_EAX)
encrypted, tag = cipher.encrypt_and_digest(message.encode())
print("Encrypted Message:")
print(base64.b64encode(encrypted).decode())

cipher2 = AES.new(key, AES.MODE_EAX, nonce=cipher.nonce)
decrypted = cipher2.decrypt(encrypted)
print("\nDecrypted Message:")
print(decrypted.decode())
