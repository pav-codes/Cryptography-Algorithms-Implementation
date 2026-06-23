from Crypto.Cipher import AES                                  #imports (AES) symmetric encryption algorithm
from Crypto.Random import get_random_bytes                     #to create a secure encryption key
import base64                                                  #converts binary data into readable text
key = get_random_bytes(16)                                     #random AES key of 16 bytes

message = "Cyber security internship project 1"
cipher = AES.new(key, AES.MODE_EAX)                            #EAX mode encrypts the data and detects if it has been modified
encrypted, tag = cipher.encrypt_and_digest(message.encode())   #converts string to bytes
print("Encrypted Message:")
print(base64.b64encode(encrypted).decode())                    #encodes encrypted message to base64

cipher2 = AES.new(key, AES.MODE_EAX, nonce=cipher.nonce)       #creates a new AES cipher object for decryption using the same key and nonce
decrypted = cipher2.decrypt(encrypted)                         #decrypts the encrypted message using the same key
print("Decrypted Message:")
print(decrypted.decode())                                      #decodes the decrypted bytes back into a string and prints it
