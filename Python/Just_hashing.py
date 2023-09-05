from hashlib import sha224

a = "I am ok".encode("utf-8")

print(sha224(a).hexdigest())