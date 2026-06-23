#SHA - hashing algoritm

import hashlib       
message = "Cyber security internship project 1"
hash_value = hashlib.sha256(message.encode()).hexdigest()

print("SHA Hash:")
print(hash_value)
