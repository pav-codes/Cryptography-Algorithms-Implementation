#RSA - asymmetric encryption algorithm

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

key = RSA.generate(2048)
public_key = key.publickey()
private_key = key
message = b"Cyber security internship project 1"

encryptor = PKCS1_OAEP.new(public_key)
encrypted = encryptor.encrypt(message)
print("Encrypted Message:",encrypted)

decryptor = PKCS1_OAEP.new(private_key)
decrypted = decryptor.decrypt(encrypted)
print("Decrypted Message:")
print(decrypted.decode())
